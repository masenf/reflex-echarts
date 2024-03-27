# reflex-echarts

A Reflex wrapper for
[echarts-for-react](https://www.npmjs.com/package/echarts-for-react) library.

## Installation

```bash
pip install reflex-echarts
```

## Usage

See [echarts_demo/echarts_demo.py](echarts_demo/echarts_demo/echarts_demo.py) for a
working example.

Props are based on the `echarts-for-react` library, so please refer to the
documentation there for further explanation.

## Themes

Themes can be set by passing a `theme` prop to the `ECharts` component.

To load custom themes, provide the JS code that ultimately calls `echarts.registerTheme` as
a string to the `register_theme_code` prop (this cannot be a State Var).

## Limitations

* Event handling is not yet implemented.
* Inline functions for formatters and data key extraction is not implemented.
  Due to how the chart `option` is serialized as JSON, there is not a clean way
  to pass inline functions from the Python backend to the Javascript frontend.
* All chart types are available, which increases the bundle size of the application.
  There is not currently a mechanism to only include the chart types which are used.
* Cannot figure out how to load external themes from a JS file...