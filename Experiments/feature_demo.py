"""Deterministic, offline demonstration of four simplified string features.

This is an educational simulation, not a FANCI implementation or evaluation.
All generated names end in .invalid. No network or DNS operations are used.
The data and numerical summaries require only the Python standard library.
The optional high-resolution illustration requires Pillow.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
import hashlib
import itertools
import json
import math
from pathlib import Path
import random
import statistics
import string
import sys


SEED = 2018
PREFIXES = (
    "campus", "student", "course", "class", "library", "research",
    "project", "faculty", "science", "school", "teacher", "lecture",
)
SUFFIXES = (
    "portal", "login", "email", "search", "notes", "forum", "cloud",
    "help", "guide", "page",
)
WORDS = (
    "amber", "apple", "beach", "birch", "bloom", "bread", "cedar",
    "charm", "coral", "crane", "creek", "dawn", "dream", "earth",
    "ember", "fern", "field", "flame", "flock", "forest", "frost",
    "glade", "grain", "green", "grove", "harbor", "hazel", "honey",
    "ivory", "lake", "leaf", "lemon", "maple", "meadow", "mist",
    "ocean", "olive", "orchard", "pearl", "pine", "pond", "quiet",
    "raven", "reed", "river", "robin", "rose", "shore", "silver",
    "sky", "snow", "song", "star", "stone", "storm", "summer",
    "sun", "trail", "valley", "water", "willow", "winter", "blossom",
    "lantern", "morning", "rainbow", "harvest", "thunder", "whisper",
    "horizon", "moonlit", "sunrise",
)
GROUPS = ("readable_control", "uniform_letters", "wordlist_pairs")
FEATURES = ("length", "vowel_ratio", "entropy_bits", "repeated_char_ratio")
LABELS = {
    "readable_control": "Đối chứng dễ đọc",
    "uniform_letters": "Ngẫu nhiên chữ cái",
    "wordlist_pairs": "Ghép từ",
}
COLORS = {
    "readable_control": "#2563EB",
    "uniform_letters": "#DC641D",
    "wordlist_pairs": "#169A80",
}


def normalized_label(domain: str) -> str:
    """Lowercase, then remove the literal suffix .invalid (not a PSL parser)."""
    lowered = domain.lower()
    if not lowered.endswith(".invalid"):
        raise ValueError("This demo accepts only its own .invalid fixtures")
    label = lowered[:-len(".invalid")]
    if not label or not set(label) <= set(string.ascii_lowercase):
        raise ValueError("Expected a non-empty a-z label")
    return label


def extract_features(domain: str) -> dict[str, int | float]:
    label = normalized_label(domain)
    counts = Counter(label)
    size = len(label)
    # Sum over DISTINCT characters, not over character occurrences.
    entropy = -sum((count / size) * math.log2(count / size)
                   for count in counts.values())
    return {
        "length": size,
        "vowel_ratio": sum(counts[c] for c in "aeiou") / size,
        "entropy_bits": entropy,
        "repeated_char_ratio": sum(count > 1 for count in counts.values()) / len(counts),
    }


def generate_rows() -> list[dict[str, str | int | float]]:
    rng = random.Random(SEED)
    controls = [prefix + suffix for prefix, suffix
                in itertools.product(PREFIXES, SUFFIXES)]
    rng.shuffle(controls)

    # Unique ordered word pairs are sampled WITHOUT replacement per length.
    # Every simulation label has exactly the length of its paired control.
    pairs_by_length: dict[int, list[str]] = defaultdict(list)
    for left, right in itertools.product(WORDS, WORDS):
        pairs_by_length[len(left) + len(right)].append(left + right)
    for size in sorted(pairs_by_length):
        pairs_by_length[size] = sorted(set(pairs_by_length[size]))
        rng.shuffle(pairs_by_length[size])

    available = {size: len(values) for size, values in pairs_by_length.items()}
    needed = Counter(map(len, controls))
    for size, count in needed.items():
        if available.get(size, 0) < count:
            raise ValueError(f"Insufficient unique word pairs for length {size}")

    random_seen: set[str] = set()
    rows: list[dict[str, str | int | float]] = []
    for pair_id, control in enumerate(controls, start=1):
        size = len(control)
        while True:
            # Offline simulation of an arithmetic-style DGA's random-looking
            # output; not an implementation of any malware DGA algorithm.
            uniform = "".join(rng.choice(string.ascii_lowercase)
                              for _ in range(size))
            if uniform not in random_seen:
                random_seen.add(uniform)
                break
        word_pair = pairs_by_length[size].pop()
        for group, label in zip(GROUPS, (control, uniform, word_pair)):
            domain = label + ".invalid"
            rows.append({
                "group": group,
                "pair_id": pair_id,
                "domain": domain,
                "normalized_label": label,
                **extract_features(domain),
            })
    return rows


def summarize(rows: list[dict]) -> dict:
    groups = {}
    for group in GROUPS:
        selected = [row for row in rows if row["group"] == group]
        groups[group] = {
            "sample_count": len(selected),
            "length_counts": dict(sorted(Counter(row["length"] for row in selected).items())),
            "features": {
                name: {
                    "mean": statistics.fmean(row[name] for row in selected),
                    # Population SD: a descriptive statistic of the full fixtures,
                    # not an estimate of variability in operational DNS data.
                    "std_population": statistics.pstdev(row[name] for row in selected),
                    "min": min(row[name] for row in selected),
                    "max": max(row[name] for row in selected),
                }
                for name in FEATURES
            },
        }
    baseline = groups["readable_control"]["features"]["entropy_bits"]
    interval_overlap = {}
    for group in GROUPS[1:]:
        stats = groups[group]["features"]["entropy_bits"]
        low, high = max(baseline["min"], stats["min"]), min(baseline["max"], stats["max"])
        interval_overlap[group] = {
            "intersection_min": low if low <= high else None,
            "intersection_max": high if low <= high else None,
            "samples_inside_control_entropy_range": sum(
                baseline["min"] <= row["entropy_bits"] <= baseline["max"]
                for row in rows if row["group"] == group
            ),
        }
    return {
        "experiment": "Offline simplified string-feature demonstration",
        "seed": SEED,
        "sample_count_total": len(rows),
        "source": "Fully synthetic fixtures defined in feature_demo.py; no DNS data",
        "groups": groups,
        "entropy_interval_overlap_with_controls": interval_overlap,
        "feature_preprocessing": "lowercase; remove literal .invalid; analyze a-z label only",
        "vowels": "aeiou",
        "entropy_unit": "bits per empirical character distribution",
        "standard_deviation": "population; denominator n",
        "python_version": sys.version.split()[0],
        "limitations": [
            "No FANCI classifier, model training, 21-feature replication, or evaluation metrics",
            "Synthetic readable controls are not verified benign NXDomain traffic",
            "Simulations do not implement or identify any real malware DGA family",
            "All labels are alphabetic and have one level before .invalid",
            "Matched lengths do not remove vocabulary and generation-process biases",
            "Entropy alone is not a measure of maliciousness or algorithmic randomness",
        ],
    }


def write_outputs(rows: list[dict], summary: dict, output_dir: Path, table_destination: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "samples_features.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    summary["csv_sha256"] = hashlib.sha256(csv_path.read_bytes()).hexdigest()
    (output_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    names = {
        "readable_control": "Đối chứng dễ đọc",
        "uniform_letters": "Mô phỏng ngẫu nhiên",
        "wordlist_pairs": "Mô phỏng ghép từ",
    }
    table = [
        "% Generated by Experiments/feature_demo.py; mean +/- population standard deviation.",
        r"\begin{tabularx}{\textwidth}{|>{\raggedright\arraybackslash}X|c|c|c|c|}",
        r"\hline",
        r"\rowcolor{LightCyan}",
        r"\textbf{Nhóm (120 mẫu)} & \textbf{$L$} & \textbf{$r_v$} & \textbf{$H$ (bit)} & \textbf{$r_r$} \\",
        r"\hline",
    ]
    for group in GROUPS:
        values = []
        for feature in FEATURES:
            stats = summary["groups"][group]["features"][feature]
            precision = 2 if feature == "length" else 3
            mean = f"{stats['mean']:.{precision}f}".replace(".", "{,}")
            std = f"{stats['std_population']:.{precision}f}".replace(".", "{,}")
            values.append(f"${mean}\\pm {std}$")
        table.append(names[group] + " & " + " & ".join(values) + r" \\ \hline")
    table.append(r"\end{tabularx}")
    table_text = "\n".join(table) + "\n"
    (output_dir / "summary_table.tex").write_text(table_text, encoding="utf-8")
    # The report's generated assets live inside Template so uploading that
    # directory alone to Overleaf keeps the report self-contained.
    table_destination.parent.mkdir(parents=True, exist_ok=True)
    table_destination.write_text(table_text, encoding="utf-8")


def draw_figure(rows: list[dict], destination: Path) -> None:
    """A publication-style PNG; Pillow is optional and is not used for statistics."""
    from PIL import Image, ImageDraw, ImageFont

    width, height = 2400, 1400
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    font_paths = (
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    )
    font_path = next((path for path in font_paths if path.exists()), None)

    def font(size: int):
        return ImageFont.truetype(str(font_path), size) if font_path else ImageFont.load_default(size=size)

    title_font, axis_font, body_font, small_font = font(60), font(48), font(46), font(44)
    foreground, muted, grid = "#152A42", "#526176", "#E6EBF1"

    def label_center(x: float, y: float, label: str, used_font=body_font, fill=muted):
        draw.text((x, y), label, anchor="mt", font=used_font, fill=fill)

    draw.text((135, 70), "Minh hoạ đặc trưng chuỗi tên miền", font=title_font, fill=foreground)
    draw.text((135, 165), "120 mẫu/nhóm | Cùng phân bố độ dài | Khởi tạo = 2018", font=body_font, fill=muted)
    lx0, lx1, rx0, rx1, y0, y1 = 150, 1090, 1370, 2290, 485, 1110
    xmin, xmax, ymin, ymax = 0.0, 0.65, 2.0, 4.1
    hmin, hmax, countmax = 2.0, 4.2, 60

    def sx(x): return lx0 + (x - xmin) / (xmax - xmin) * (lx1 - lx0)
    def sy(y): return y1 - (y - ymin) / (ymax - ymin) * (y1 - y0)
    def hx(x): return rx0 + (x - hmin) / (hmax - hmin) * (rx1 - rx0)
    def hy(y): return y1 - y / countmax * (y1 - y0)

    label_center((lx0+lx1)/2, 335, "(a) Tỷ lệ nguyên âm và entropy", axis_font, foreground)
    label_center((rx0+rx1)/2, 335, "(b) Phân bố entropy", axis_font, foreground)

    for x in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6):
        px = sx(x)
        draw.line((px, y0, px, y1), fill=grid, width=2)
        label_center(px, y1+22, f"{x:.1f}".replace(".", ","), small_font)
    for y in (2.0, 2.5, 3.0, 3.5, 4.0):
        py = sy(y)
        draw.line((lx0, py, lx1, py), fill=grid, width=2)
        draw.text((lx0-22, py), f"{y:.1f}".replace(".", ","), anchor="rm", font=small_font, fill=muted)
    for x in (2.0, 2.4, 2.8, 3.2, 3.6, 4.0):
        px = hx(x)
        draw.line((px, y0, px, y1), fill=grid, width=2)
        label_center(px, y1+22, f"{x:.1f}".replace(".", ","), small_font)
    for y in range(0, countmax+1, 10):
        py = hy(y)
        draw.line((rx0, py, rx1, py), fill=grid, width=2)
        draw.text((rx0-22, py), str(y), anchor="rm", font=small_font, fill=muted)
    for xleft, xright in ((lx0, lx1), (rx0, rx1)):
        draw.line((xleft, y0, xleft, y1, xright, y1), fill=foreground, width=3)
    label_center((lx0+lx1)/2, y1+100, "Tỷ lệ nguyên âm (a, e, i, o, u)", axis_font)
    label_center((rx0+rx1)/2, y1+100, "Entropy Shannon (bit)", axis_font)
    draw.text((lx0, y0-70), "Entropy (bit)", font=body_font, fill=muted)
    draw.text((rx0, y0-70), "Số mẫu", font=body_font, fill=muted)
    draw.text((rx1, y0-70), "Khoảng chia: 0,2 bit", anchor="rt", font=small_font, fill=muted)

    # Add marker-shape distinction for grayscale and color-vision accessibility.
    def marker(x, y, group, radius=8):
        color = COLORS[group]
        if group == "readable_control":
            draw.ellipse((x-radius, y-radius, x+radius, y+radius), outline=color, width=3)
        elif group == "uniform_letters":
            draw.polygon(((x, y-radius-1), (x-radius-1, y+radius), (x+radius+1, y+radius)), outline=color, width=3)
        else:
            draw.rectangle((x-radius, y-radius, x+radius, y+radius), outline=color, width=3)

    for row in rows:
        marker(sx(row["vowel_ratio"]), sy(row["entropy_bits"]), row["group"])

    edges = [hmin + 0.2 * idx for idx in range(12)]
    for group in GROUPS:
        selected = [row["entropy_bits"] for row in rows if row["group"] == group]
        counts = [sum(left <= value < right for value in selected)
                  for left, right in zip(edges, edges[1:])]
        if max(counts) > countmax:
            raise ValueError("Histogram exceeds the declared axis range")
        for index, count in enumerate(counts):
            # Grouped bars prevent opacity or draw order from hiding overlap.
            group_index = GROUPS.index(group)
            span = (hx(edges[index+1]) - hx(edges[index])) / 3
            left = hx(edges[index]) + group_index * span + 2
            right = left + span - 4
            draw.rectangle((left, hy(count), right, y1), fill=COLORS[group])

    legend_positions = (150, 825, 1640)
    for group, x in zip(GROUPS, legend_positions):
        marker(x+15, 280, group, 14)
        draw.text((x+50, 280), LABELS[group], anchor="lm", font=body_font, fill=foreground)
    destination.parent.mkdir(parents=True, exist_ok=True)
    img.save(destination, dpi=(300, 300), optimize=True)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=root / "Experiments" / "results")
    parser.add_argument("--figure", type=Path, default=root / "Template" / "Figures" / "Chuong4_MinhHoaDacTrung.png")
    parser.add_argument("--table", type=Path, default=root / "Template" / "Figures" / "Bang4_MinhHoaDacTrung.tex")
    parser.add_argument("--no-figure", action="store_true", help="Generate standard-library CSV/JSON/TeX only")
    args = parser.parse_args()
    rows = generate_rows()
    summary = summarize(rows)
    write_outputs(rows, summary, args.output_dir, args.table)
    if not args.no_figure:
        try:
            draw_figure(rows, args.figure)
        except ImportError:
            print("Pillow is unavailable: numerical outputs saved; use --no-figure or install Pillow for the PNG.", file=sys.stderr)
            raise SystemExit(2)
    print(json.dumps({
        "seed": SEED,
        "samples": len(rows),
        "csv_sha256": summary["csv_sha256"],
        "output_dir": str(args.output_dir),
        "figure": str(args.figure) if not args.no_figure else None,
        "table": str(args.table),
        "mean_entropy_bits": {
            group: summary["groups"][group]["features"]["entropy_bits"]["mean"]
            for group in GROUPS
        },
    }, indent=2))


if __name__ == "__main__":
    main()
