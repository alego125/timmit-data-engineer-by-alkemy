This is a mermaid diagram, you may need to install a [Browser Plugin](https://github.com/BackMarket/github-mermaid-extension) or [VsCode extension](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) or similar to view it.

You can also [view it full screen as an SVG](https://mermaid.ink/svg/c2VxdWVuY2VEaWFncmFtCiAgc3RhcnQtPj5DYWxjdWxhZG9yYS5hZGQ6IGNhbGxzIHg0CiAgQ2FsY3VsYWRvcmEuYWRkLS0+PnN0YXJ0OiByZXR1cm5zIGZsb2F0CiAgc3RhcnQtPj5DYWxjdWxhZG9yYS5zdWJ0cmFjdDogY2FsbHMgeDYKICBDYWxjdWxhZG9yYS5zdWJ0cmFjdC0tPj5zdGFydDogcmV0dXJucyBmbG9hdAo=)        

```mermaid
sequenceDiagram
  start->>Calculadora.add: calls x4
  Calculadora.add-->>start: returns float
  start->>Calculadora.subtract: calls x6
  Calculadora.subtract-->>start: returns float

```
