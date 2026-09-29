# 发布文件清单

以下清单是本次公开仓库的完整加入范围；未列出的本地文件、目录与历史版本均排除。

| 处置 | 仓库路径 | 内容与核对 |
|---|---|---|
| ADD | `README.md`、`SKILL.md`、`verify.py` | 独立 Skill 入口、使用说明与资源验证脚本。 |
| ADD | `agents/openai.yaml` | Skill 在 Codex 中显示的名称、简介与默认调用提示。 |
| ADD | `references/people.md`、`references/giants.md`、`references/cases.md` | 人物与东方巨构分支指南、案例索引。 |
| ADD | `references/images/person-umber-incense.jpg`、`person-vermilion-scroll.jpg`、`person-deep-teal-pond.jpg`、`person-indigo-tea.jpg` | 人物分支四张不同主导色代表图。 |
| ADD | `references/images/giant-sand-palace.jpg`、`giant-russet-wall.jpg`、`giant-dark-green-cloth.jpg`、`giant-pale-bone.jpg`、`giant-midnight-palace.jpg` | 巨构分支五张不同主导色代表图。 |
| ADD | `showcase/README.md`、`showcase/POSTER-BRIEF.md`、`showcase/PUBLICATION-MANIFEST.md`、`showcase/source-hashes.json` | 海报介绍、逐页锚点、发布清单与案例图哈希。 |
| ADD | `showcase/posters/01.png`–`06.png`、`contact.jpg`、`posters.html`、`render.js` | 六张 1080 × 1920 可编辑排版海报、总览与源文件。 |
| ADD | `showcase/posters-image/01.png`–`06.png`、`contact.jpg`、`mineral-paper-bg.png`、`posters.html`、`render.js` | 六张 1080 × 1920 Image 材质底版、总览与源文件。 |
| ADD | `showcase/posters-image-art/01.png`–`06.png`、`overview.jpg`、`README.md`、`status.json` | 六张 941 × 1672 全画面艺术海报、总览及状态说明。 |
| EXCLUDE | 未列出的全部文件 | 排除原始素材目录、旧替换稿、剪贴板文件、临时 patch、回滚脚本、操作日志及含本机路径的溯源材料。 |

## 发布核对

- 人物 4 张、巨构 5 张；各分支主导色互不重复，案例图哈希与文件内容一致。
- 三套海报共 18 张；可编辑版及材质底版为 1080 × 1920，艺术版为 941 × 1672。
- 两套 HTML 海报源码中的图片路径已修正；浏览器加载检查通过，两组共 12 张渲染输出与现有 PNG 哈希一致。
- 所有公开文档使用相对路径。仓库未为全部素材声明统一许可证；案例图与作品素材的权利归相应创作者，公开转载或商业使用前请逐项确认使用权。
