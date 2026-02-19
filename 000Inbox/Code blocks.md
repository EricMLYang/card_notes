---
tags:
  - heptabase-tutorial
Level:
  - Beginner
Type:
  - Basic Operations
Component:
  - Card
---
# Code blocks

## Tips

1. To create a code block, type `/` and then type `code`

2. To turn a text into an inline code, press `Cmd/Ctrl` + `E`

## Examples

Let’s define 2 new functions called `add` and `printResult`:

```ts
function add(n1: number, n2: number): number {
    return n1 + n2;
}

function printResult(num: number): void {
    console.log('Result: ' + num);
}
```