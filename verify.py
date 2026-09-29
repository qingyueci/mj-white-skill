from pathlib import Path
from PIL import Image
import hashlib, json, re

repo = Path(__file__).resolve().parent
show = repo / "showcase"
skill = repo
required = [repo / "SKILL.md", repo / "references/people.md", repo / "references/giants.md",
            repo / "references/cases.md", repo / "README.md", show / "README.md",
            show / "POSTER-BRIEF.md", show / "PUBLICATION-MANIFEST.md", show / "source-hashes.json"]
assert all(p.is_file() and p.stat().st_size for p in required)
print("FILES=PASS")

frontmatter = re.match(r"^---\n(.*?)\n---", (repo / "SKILL.md").read_text(encoding="utf-8"), re.S)
assert frontmatter and re.search(r"^name: mj-white-skill$", frontmatter.group(1), re.M)
assert re.search(r"^description: .+", frontmatter.group(1), re.M)
for path in required[:8]:
    for link in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
        if not link.startswith(("http:", "https:")):
            assert (path.parent / link.split("#")[0]).exists(), (path, link)
print("SKILL_HEADER_AND_LINKS=PASS")

for html_path in (show / "posters/posters.html", show / "posters-image/posters.html"):
    html = html_path.read_text(encoding="utf-8")
    references = re.findall(r'src=["\']([^"\']+)', html)
    references += re.findall(r'url\(["\']?([^\)"\']+)', html)
    for reference in references:
        if not reference.startswith(("http:", "https:", "data:", "#")):
            assert (html_path.parent / reference).is_file(), (html_path, reference)
print("SHOWCASE_SOURCE_ASSETS=PASS")

assets = json.loads((show / "source-hashes.json").read_text(encoding="utf-8"))["selected_assets"]
assert len(assets) == 9
assert sum(a["branch"] == "人物" for a in assets) == 4
assert sum(a["branch"] == "巨构" for a in assets) == 5
for branch in ("人物", "巨构"):
    group = [a for a in assets if a["branch"] == branch]
    assert len({a["color"] for a in group}) == len(group)
for asset in assets:
    image_path = repo / asset["asset"]
    assert image_path.is_file() and hashlib.sha256(image_path.read_bytes()).hexdigest() == asset["asset_sha256"]
    with Image.open(image_path) as im:
        im.verify()
print("CASES=PASS; PERSON=4; GIANT=5; UNIQUE_COLORS=PASS; HASHES=PASS")

assert "无人物" in (show / "POSTER-BRIEF.md").read_text(encoding="utf-8")
poster_sizes = {"posters": (1080, 1920), "posters-image": (1080, 1920), "posters-image-art": (941, 1672)}
for folder, expected_size in poster_sizes.items():
    for number in range(1, 7):
        image_path = show / folder / f"{number:02d}.png"
        assert image_path.is_file() and image_path.stat().st_size > 1000
        with Image.open(image_path) as im:
            assert im.size == expected_size, (image_path, im.size)
            im.verify()
assert (show / "posters-image-art/overview.jpg").is_file()
assert len(json.loads((show / "posters-image-art/status.json").read_text(encoding="utf-8"))["completed"]) == 6
html_cover = (show / "posters/posters.html").read_text(encoding="utf-8").split('<section class="poster p2"')[0]
assert "person-umber-incense.jpg" not in html_cover
for path in required[4:] + [show / "posters-image-art/README.md", show / "posters-image-art/status.json"]:
    assert not re.search(r"[A-Za-z]:[\\/]", path.read_text(encoding="utf-8")), path
print("POSTERS=PASS; SETS=3; PAGES=18; DIMENSIONS=2x1080x1920+1x941x1672")
print("COVER=TEXT_ONLY; PUBLIC_TEXT=NO_LOCAL_PATHS")
