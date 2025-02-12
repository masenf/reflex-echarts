"""Wrapper for echarts-for-react library."""

from typing import Dict, Optional

import reflex as rx


class Echarts(rx.Component):
    """ReactECharts component.

    Usage:
        Set any echarts option dict to the option prop. The chart will update when the
        option data updates.

    See https://www.npmjs.com/package/echarts-for-react for explanation of props.
    See https://echarts.apache.org/examples/en/index.html for echarts examples.
    """

    library = "echarts-for-react@^3.0.2"

    # The React component tag.
    tag = "ReactECharts"

    is_default = True

    # the echarts option config, can see https://echarts.apache.org/option.html#title.
    option: rx.Var[Dict]

    # when setOption, not merge the data, default is false. See https://echarts.apache.org/api.html#echartsInstance.setOption.
    not_merge: rx.Var[bool]

    # when setOption, lazy update the data, default is false. See https://echarts.apache.org/api.html#echartsInstance.setOption.
    lazy_update: rx.Var[bool]

    # the echarts loading option config, can see https://echarts.apache.org/api.html#echartsInstance.showLoading.
    loading_option: rx.Var[Dict]

    # bool, when the chart is rendering, show the loading mask.
    show_loading: rx.Var[bool]

    # the theme of echarts. string
    theme: rx.Var[str]

    # The code that should be executed to register a theme
    register_theme_code: Optional[str] = None

    # the opts of echarts. object, will be used when initial echarts instance by echarts.init. Document here.
    opts: rx.Var[Dict]

    # Fired when the chart is ready
    on_chart_ready: rx.EventHandler[rx.event.no_args_event_spec]

    @classmethod
    def create(cls, *children, **props):
        """Create a ReactECharts component.

        Args:
            *children: The children of the component.
            **props: The properties of the component.

        Returns:
            The ReactECharts component.

        """
        props["width"] = props.pop("width", "100%")
        return super().create(*children, **props)

    def _exclude_props(self) -> list[str]:
        return [*super()._exclude_props(), "register_theme_code"]

    def add_imports(self) -> rx.ImportDict:
        return {
            "echarts": [rx.ImportVar(tag="* as echarts", is_default=True)],
        }

    def add_custom_code(self) -> list[str]:
        if self.register_theme_code is not None:
            return [self.register_theme_code]
        return []


echarts = Echarts.create
