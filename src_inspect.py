import os
import glob
import pandas as pd
import numpy as np

def build_inventory_and_quality():
    raw_dir = "SKAB/data/raw/SKAB/data"
    csv_files = glob.glob(os.path.join(raw_dir, "**/*.csv"), recursive=True)
    csv_files = sorted([f.replace("\\", "/") for f in csv_files])
    
    print(f"Bulunan CSV dosya sayısı: {len(csv_files)}")
    
    inventory_rows = []
    column_quality_rows = []
    
    for fpath in csv_files:
        rel_path = os.path.relpath(fpath, "SKAB/data/raw/SKAB").replace("\\", "/")
        exp_id = rel_path.replace("data/", "").replace(".csv", "")
        
        # Ayrıştırma kontrolü
        try:
            df = pd.read_csv(fpath, sep=";")
        except Exception as e:
            print(f"HATA: {fpath} okunamadı: {e}")
            continue
            
        n_rows, n_cols = df.shape
        cols = list(df.columns)
        
        # datetime analizi
        has_dt = "datetime" in df.columns
        invalid_missing_dt = 0
        is_monotonic = None
        dup_dt = 0
        dt_min = dt_max = dt_median = dt_mean = None
        start_time = end_time = None
        
        if has_dt:
            # parse datetime
            dt_series = pd.to_datetime(df["datetime"], errors="coerce")
            invalid_missing_dt = int(dt_series.isna().sum())
            dup_dt = int(dt_series.duplicated().sum())
            
            valid_dt = dt_series.dropna()
            if len(valid_dt) > 0:
                start_time = str(valid_dt.iloc[0])
                end_time = str(valid_dt.iloc[-1])
                is_monotonic = bool(valid_dt.is_monotonic_increasing)
                
                # dt hesaplama (saniye)
                diffs = valid_dt.diff().dt.total_seconds().dropna()
                if len(diffs) > 0:
                    dt_min = float(diffs.min())
                    dt_max = float(diffs.max())
                    dt_median = float(diffs.median())
                    dt_mean = float(diffs.mean())
        
        # Etiket analizi
        has_anomaly = "anomaly" in df.columns
        anomaly_0 = anomaly_1 = None
        anomaly_vals = None
        if has_anomaly:
            anom_counts = df["anomaly"].value_counts(dropna=False).to_dict()
            anomaly_0 = anom_counts.get(0.0, anom_counts.get(0, 0))
            anomaly_1 = anom_counts.get(1.0, anom_counts.get(1, 0))
            anomaly_vals = str(list(df["anomaly"].unique()))
            
        has_changepoint = "changepoint" in df.columns
        changepoint_0 = changepoint_1 = None
        changepoint_vals = None
        if has_changepoint:
            cp_counts = df["changepoint"].value_counts(dropna=False).to_dict()
            changepoint_0 = cp_counts.get(0.0, cp_counts.get(0, 0))
            changepoint_1 = cp_counts.get(1.0, cp_counts.get(1, 0))
            changepoint_vals = str(list(df["changepoint"].unique()))
            
        # Toplam eksik değer
        total_missing = int(df.isna().sum().sum())
        missing_by_col = {c: int(df[c].isna().sum()) for c in df.columns if df[c].isna().sum() > 0}
        
        inventory_rows.append({
            "relative_path": rel_path,
            "experiment_id": exp_id,
            "row_count": n_rows,
            "col_count": n_cols,
            "columns": ";".join(cols),
            "start_time": start_time,
            "end_time": end_time,
            "invalid_or_missing_datetime": invalid_missing_dt,
            "is_strictly_monotonic_datetime": is_monotonic,
            "duplicate_datetimes": dup_dt,
            "dt_min_sec": dt_min,
            "dt_median_sec": dt_median,
            "dt_max_sec": dt_max,
            "dt_mean_sec": dt_mean,
            "total_missing_values": total_missing,
            "missing_cols_detail": str(missing_by_col) if missing_by_col else "None",
            "has_anomaly_col": has_anomaly,
            "anomaly_0_count": anomaly_0,
            "anomaly_1_count": anomaly_1,
            "anomaly_unique_vals": anomaly_vals,
            "has_changepoint_col": has_changepoint,
            "changepoint_0_count": changepoint_0,
            "changepoint_1_count": changepoint_1,
            "changepoint_unique_vals": changepoint_vals,
        })
        
        # Kolon bazlı kalite istatistikleri
        numeric_cols = [c for c in df.columns if c not in ["datetime", "anomaly", "changepoint"]]
        for c in numeric_cols:
            col_data = pd.to_numeric(df[c], errors="coerce")
            n_nan = int(col_data.isna().sum())
            n_zero = int((col_data == 0).sum())
            val_min = float(col_data.min()) if col_data.count() > 0 else np.nan
            val_max = float(col_data.max()) if col_data.count() > 0 else np.nan
            val_mean = float(col_data.mean()) if col_data.count() > 0 else np.nan
            val_std = float(col_data.std()) if col_data.count() > 0 else np.nan
            
            # Sabit kalma (stuck-at) kontrolü: aralıksız aynı değeri alma max uzunluğu
            diff_zero = (col_data.diff() == 0).astype(int)
            # consecutive zeros in diff
            max_stuck = 0
            curr_stuck = 0
            for is_same in (col_data.diff() == 0):
                if is_same:
                    curr_stuck += 1
                    if curr_stuck > max_stuck:
                        max_stuck = curr_stuck
                else:
                    curr_stuck = 0
            # +1 çünkü diff=0 ise en az 2 değer aynıdır
            max_stuck = max_stuck + 1 if max_stuck > 0 else 1
            
            column_quality_rows.append({
                "experiment_id": exp_id,
                "column_name": c,
                "data_type": str(df[c].dtype),
                "count": int(col_data.count()),
                "missing_count": n_nan,
                "zero_count": n_zero,
                "min": val_min,
                "max": val_max,
                "mean": round(val_mean, 4) if not np.isnan(val_mean) else np.nan,
                "std": round(val_std, 4) if not np.isnan(val_std) else np.nan,
                "max_consecutive_constant_samples": max_stuck
            })

    inv_df = pd.DataFrame(inventory_rows)
    inv_df.to_csv("results/data_review/inventory.csv", index=False)
    print("inventory.csv oluşturuldu.")
    
    cq_df = pd.DataFrame(column_quality_rows)
    cq_df.to_csv("results/data_review/column_quality.csv", index=False)
    print("column_quality.csv oluşturuldu.")
    
    print("\n--- Özet Bilgiler ---")
    print(f"Toplam dosya sayısı: {len(inv_df)}")
    print(f"Etiketsiz dosya sayısı: {len(inv_df[~inv_df['has_anomaly_col']])}")
    print(f"Zaman sırası monoton olmayan dosya sayısı: {len(inv_df[inv_df['is_strictly_monotonic_datetime'] == False])}")
    print(f"Tekrarlanan zaman damgası olan dosya sayısı: {len(inv_df[inv_df['duplicate_datetimes'] > 0])}")
    print(f"Eksik değer içeren dosya sayısı: {len(inv_df[inv_df['total_missing_values'] > 0])}")
    print(f"Ortalama satır sayısı: {inv_df['row_count'].mean():.1f} (min: {inv_df['row_count'].min()}, max: {inv_df['row_count'].max()})")

if __name__ == "__main__":
    build_inventory_and_quality()
