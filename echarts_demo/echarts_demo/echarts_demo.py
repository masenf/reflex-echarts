import random

import httpx

import reflex as rx

from reflex_echarts import echarts

from . import themes


ROOT_PATH = "https://echarts.apache.org/examples"
_response = httpx.get(f"{ROOT_PATH}/data/asset/data/life-expectancy-table.json")
_response.raise_for_status()
_rawData = _response.json()


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

    def munge_line_chart(self):
        self.line_chart["series"][0]["data"] = [
            random.randint(120, 280) for _ in range(7)
        ]

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
        datasetWithFilters = []
        seriesList = []
        for country in countries:
            datasetId = "dataset_" + country
            datasetWithFilters.append(
                {
                    "id": datasetId,
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
            seriesList.append(
                {
                    "type": "line",
                    "datasetId": datasetId,
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
            "dataset": [{"id": "dataset_raw", "source": _rawData}, *datasetWithFilters],
            "title": {"text": "Income of Germany and France since 1950"},
            "tooltip": {"order": "valueDesc", "trigger": "axis"},
            "xAxis": {"type": "category", "nameLocation": "middle"},
            "yAxis": {"name": "Income"},
            "grid": {"right": 140},
            "series": seriesList,
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
