# Extracted from theme js files on https://echarts.apache.org/en/download-theme.html

# Pass these values for `register_theme_code` prop, then set the theme name in
# the `theme` prop.

vintage = """
var colorPalette = [
    '#d87c7c',
    '#919e8b',
    '#d7ab82',
    '#6e7074',
    '#61a0a8',
    '#efa18d',
    '#787464',
    '#cc7e63',
    '#724e58',
    '#4b565b'
];
echarts.registerTheme('vintage', {
    color: colorPalette,
    backgroundColor: '#fef8ef',
    graph: {
        color: colorPalette
    }
});"""


roma = """
    var colorPalette = [
        '#E01F54',
        '#001852',
        '#f5e8c8',
        '#b8d2c7',
        '#c6b38e',
        '#a4d8c2',
        '#f3d999',
        '#d3758f',
        '#dcc392',
        '#2e4783',
        '#82b6e9',
        '#ff6347',
        '#a092f1',
        '#0a915d',
        '#eaf889',
        '#6699FF',
        '#ff6666',
        '#3cb371',
        '#d5b158',
        '#38b6b6'
    ];

    var theme = {
        color: colorPalette,

        visualMap: {
            color: ['#e01f54', '#e7dbc3'],
            textStyle: {
                color: '#333'
            }
        },

        candlestick: {
            itemStyle: {
                color: '#e01f54',
                color0: '#001852'
            },
            lineStyle: {
                width: 1,
                color: '#f5e8c8',
                color0: '#b8d2c7'
            },
            areaStyle: {
                color: '#a4d8c2',
                color0: '#f3d999'
            }
        },

        graph: {
            itemStyle: {
                color: '#a4d8c2'
            },
            linkStyle: {
                color: '#f3d999'
            }
        },

        gauge: {
            axisLine: {
                lineStyle: {
                    color: [
                        [0.2, '#E01F54'],
                        [0.8, '#b8d2c7'],
                        [1, '#001852']
                    ],
                    width: 8
                }
            }
        }
    };

    echarts.registerTheme('roma', theme);
"""
