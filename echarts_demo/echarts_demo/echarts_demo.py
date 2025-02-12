import json
import random
from pathlib import Path

import reflex as rx
from reflex_echarts import echarts

from . import themes

# https://echarts.apache.org/examples/data/asset/data/life-expectancy-table.json
with (Path(__file__).parent / "life-expectancy-table.json").open("r") as f:
    _raw_data = json.load(f)


class State(rx.State):
    """The app state."""

    line_chart: dict = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [{"data": [150, 230, 224, 218, 135, 147, 260], "type": "line"}],
    }

    country_income_race: dict = {}

    @rx.event
    def munge_line_chart(self):
        self.line_chart["series"][0]["data"] = [
            random.randint(120, 280) for _ in range(7)
        ]

    @rx.event
    def on_load(self):
        countries = [
            "Finland",
            "France",
            "Germany",
            "Iceland",
            "Norway",
            "Poland",
            "Russia",
            "United Kingdom",
        ]
        dataset_with_filters = []
        series_list = []
        for country in countries:
            dataset_id = "dataset_" + country
            dataset_with_filters.append(
                {
                    "id": dataset_id,
                    "fromDatasetId": "dataset_raw",
                    "transform": {
                        "type": "filter",
                        "config": {
                            "and": [
                                {"dimension": "Year", "gte": 1950},
                                {"dimension": "Country", "=": country},
                            ]
                        },
                    },
                }
            )
            series_list.append(
                {
                    "type": "line",
                    "datasetId": dataset_id,
                    "showSymbol": False,
                    "name": country,
                    "endLabel": {
                        "show": True,
                    },
                    "labelLayout": {"moveOverlap": "shiftY"},
                    "emphasis": {"focus": "series"},
                    "encode": {
                        "x": "Year",
                        "y": "Income",
                        "label": ["Country", "Income"],
                        "itemName": "Year",
                        "tooltip": ["Income"],
                    },
                }
            )

        self.country_income_race = {
            "animationDuration": 10000,
            "dataset": [
                {"id": "dataset_raw", "source": _raw_data},
                *dataset_with_filters,
            ],
            "title": {"text": "Income of European countries since 1950"},
            "tooltip": {"order": "valueDesc", "trigger": "axis"},
            "xAxis": {"type": "category", "nameLocation": "middle"},
            "yAxis": {"name": "Income"},
            "grid": {"right": 140},
            "series": series_list,
        }


def index() -> rx.Component:
    return rx.vstack(
        echarts(option=State.line_chart, theme="dark"),
        rx.button("New Data for Line Chart", on_click=State.munge_line_chart),
        rx.divider(),
        echarts(
            option=State.country_income_race,
            register_theme_code=themes.roma,
            theme="roma",
            on_chart_ready=rx.console_log("Country income chart is ready"),
        ),
        align="center",
        width="100vw",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index, on_load=State.on_load)
