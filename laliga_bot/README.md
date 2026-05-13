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


## Polymarket adaptor (MVP)
Gunakan `laliga_bot.polymarket` untuk menghitung implied probability dan edge decision (take/skip) berdasarkan threshold minimum edge.


## Setup cepat environment
Jika dependency belum terpasang, jalankan:
```bash
./scripts_setup_env.sh
```

Atau manual:
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r laliga_bot/requirements.txt
python -m unittest discover -s tests
```

Jika instalasi gagal karena pembatasan network/proxy di environment, lakukan setup di mesin lokal atau CI runner yang punya akses ke PyPI.
