---
tags:
  - heptabase-tutorial
Level:
  - Expert
Type:
  - Advanced Guide
Component:
  - Whiteboard
---
# [Nested Whiteboard](https://wiki.heptabase.com/nested-whiteboard): Organize learning topics with hierarchies and reusable cards.

![](https://imgur.com/Sqi8SOJ.png)

In traditional note-taking apps, you often need to use a folder-based hierarchical structure to manage your notes. However, the drawback of this structure is that as you accumulate more notes, **it becomes easy to get lost in the vast number of layers, and changing the folder structure can become very difficult.**

In contrast, some modern note-taking apps advocate for eliminating all hierarchies and instead establishing bi-directional links between notes, allowing all notes to be interconnected in a giant graph. However, as this graph grows larger, **you may find it increasingly difficult to maintain a sense of direction and locate your notes.**

Heptabase has achieved a perfect balance between hierarchical structure and graph structure by integrating the designs of "nested whiteboard" and "graph-based card library."

Let's imagine for a moment that you have accumulated around ten thousand notes over the years. How would you manage them across different note-taking apps?

- In a hierarchical note-taking app, once you have more than twenty notes in a folder, you will start to feel disorganized. If you have about ten thousand notes, you will need to use at least three to four layers of folders to manage them, which makes finding things quite inconvenient. If one day you feel that the current folder structure is not suitable anymore, you will need to spend at least an entire week designing a new folder structure and then move all the notes from the existing folders into this new folder structure. This process is very painful and time-consuming.

- In a graph-based note-taking app, these ten thousand notes form a giant graph. You will find that your memory gradually cannot keep up with the size of this graph. Many times, you can't even remember what notes you have written and can only rely on keyword searches in the end. The sense of "stability" brought by hierarchical management does not exist in a pure graph structure.

In contrast, in Heptabase, you may start to feel overwhelmed when you have more than a hundred cards on each whiteboard. Assuming you have ten parent whiteboards on the top level, each containing ten child whiteboards, and each whiteboard has about a hundred cards, with this structure, you can manage over ten thousand notes with just two layers of hierarchy. Finding notes will become much easier!

Moreover, in the world of folders, every file belongs to a folder, but in Heptabase, cards and whiteboards are independent of each other. A card can appear in multiple whiteboards at the same time. Although the structure of the whiteboard is hierarchical, the relationships between cards are a graph.

In other words, if you are not satisfied with the current whiteboard structure, you can always create a new one without altering the existing structure, and then reuse the existing cards in the new structure. This flexibility allows you to gradually evolve your whiteboard structure over time, without having to spend an entire week moving and reorganizing all your notes.

## **How to use nested whiteboard**

To create a sub-whiteboard within a whiteboard, the most straightforward way is to right-click on an empty space of the whiteboard and choose the option "Whiteboard" to add a sub-whiteboard.

![](https://imgur.com/eMK8jKA.png)

When you are in a whiteboard, you can check which layer the whiteboard is in the hierarchy through the breadcrumb in the top left corner of the whiteboard. Taking the following image as an example, "The Dream Machine" is a sub-whiteboard of "Reading Notes."

![](https://imgur.com/VBQBQrp.png)

In most cases, the relationship between the nested whiteboards represents the relationship between topics. For example, you may have a whiteboard called "Science," and inside it, there are sub-whiteboards such as "Physics," "Chemistry," "Biology," and so on.

## **How to reuse cards across whiteboards**

If you want to reuse cards that have been used on other whiteboards, there are two common methods:

1. Simply click on the button in the top right corner of the whiteboard to access the Card Library. Search for the card and drag it onto the whiteboard.

2. In another whiteboard, select the cards you want, right-click, and choose "Copy". Then go to your target whiteboard, right-click, and choose "Paste". Select the option "Sync pasted card" while pasting.

For example, you may have a card related to genetic science, and you can place it on both the "Genetic engineering" and "Biology" whiteboards. If you have a card related to the US reserve currency, you can also place it on both the "US history" and "Macroeconomics" whiteboards.