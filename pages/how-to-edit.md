---
title: How to Edit This Wiki
nav_order: 2
---

# How to Edit This Wiki

You need to be signed in to GitHub as the owner of this wiki. Visitors can read everything, but they can't change anything.

## Make a new page

1. Click **+ New page** in the top-right corner of the wiki.
2. GitHub opens with a starter page already filled in.
3. Change the file name at the top (for example `camping-gear.md`). Use lowercase letters and dashes, and end it with `.md`.
4. Change `title: My New Page` to the name you want in the sidebar.
5. Write your page below the second `---` line.
6. Click **Commit changes…**, then **Commit changes** again.

The page shows up on the wiki about a minute later. Refresh to see it.

## Edit a page

Scroll to the bottom of any page and click **Edit this page on GitHub**. Make your changes and click **Commit changes**.

## Delete a page

Open the page's file on GitHub (in the `pages` folder), click the **…** menu, and choose **Delete file**.

## Formatting cheat sheet

Pages are written in Markdown, which is plain text with a few symbols:

| You type | You get |
|---|---|
| `# Big heading` | A large heading |
| `## Smaller heading` | A section heading |
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `- item` | A bullet point |
| `1. item` | A numbered list |
| `[link text](https://example.com)` | [link text](https://example.com) |
| `[another page](camping-gear)` | A link to another wiki page |
| `![description](../images/photo.jpg)` | A picture |

## Add a picture

1. On GitHub, open the `images` folder.
2. Click **Add file** → **Upload files**, drag your picture in, and click **Commit changes**.
3. In your page, write `![description](../images/your-photo.jpg)`.

## Change the order in the sidebar

Add a `nav_order` line under the title. Lower numbers appear higher in the sidebar:

```
---
title: Camping Gear
nav_order: 5
---
```
