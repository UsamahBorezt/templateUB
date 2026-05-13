import argparse

from laliga_bot.config import OUTPUT_DIR
from laliga_bot.data_pipeline import load_matches
from laliga_bot.features import add_target_label, add_team_form_features
from laliga_bot.model import load_model, predict_proba, train_model


def run_train(data_path: str) -> None:
    df = load_matches(data_path)
    df_feat = add_team_form_features(df)
    df_labeled = add_target_label(df_feat)
    train_model(df_labeled)
    print("Training selesai. Model tersimpan.")


def run_predict(data_path: str, limit: int) -> None:
    df = load_matches(data_path)
    df_feat = add_team_form_features(df)
    pipe = load_model()
    pred = predict_proba(pipe, df_feat.tail(limit))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUTPUT_DIR / "predictions.csv"
    pred.to_csv(out_file, index=False)
    print(f"Prediksi disimpan ke: {out_file}")


def main() -> None:
    parser = argparse.ArgumentParser(description="LaLiga W/D/L prediction bot")
    sub = parser.add_subparsers(dest="cmd", required=True)

    train = sub.add_parser("train")
    train.add_argument("--data", required=True)

    pred = sub.add_parser("predict")
    pred.add_argument("--data", required=True)
    pred.add_argument("--limit", type=int, default=10)

    args = parser.parse_args()

    if args.cmd == "train":
        run_train(args.data)
    elif args.cmd == "predict":
        run_predict(args.data, args.limit)


if __name__ == "__main__":
    main()
