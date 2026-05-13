# LaLiga Prediction Bot (MVP)

MVP bot untuk memprediksi peluang **Home / Draw / Away** sebelum pertandingan dimulai.

## Workflow
1. `fetch` data historis pertandingan (CSV lokal untuk MVP).
2. `build_features` dari data yang tersedia pre-match.
3. `train` model klasifikasi 3 kelas.
4. `predict` untuk pertandingan berikutnya.

## Struktur
- `config.py` — konfigurasi path dan parameter model.
- `data_pipeline.py` — validasi + loading data.
- `features.py` — feature engineering rolling form.
- `model.py` — training model dan prediksi probabilitas.
- `main.py` — CLI sederhana untuk train dan predict.

## Format data input
CSV minimal harus berisi kolom:
- `date` (YYYY-MM-DD)
- `home_team`
- `away_team`
- `home_goals`
- `away_goals`

Contoh hasil disimpan ke:
- model: `laliga_bot/models/wdl_model.joblib`
- prediksi: `laliga_bot/output/predictions.csv`

## Jalankan
```bash
python -m laliga_bot.main train --data /path/to/matches.csv
python -m laliga_bot.main predict --data /path/to/upcoming_or_recent.csv --limit 10
```
