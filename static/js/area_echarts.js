
$(function () {
    map();
    function map() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('map_1'));
var data = geo.geo_1;
// var data = [{'name': '北京', 'value': 86125}, {'name': '深圳', 'value': 53724}, {'name': '上海', 'value': 51500}, {'name': '成都', 'value': 37454}, {'name': '广州', 'value': 36396}, {'name': '杭州', 'value': 22828}, {'name': '武汉', 'value': 18921}, {'name': '济南', 'value': 17944}, {'name': '天津', 'value': 11118}, {'name': '青岛', 'value': 8133}]

var geoCoordMap = {
    '青岛':[120.33,36.07],
    '广州':[113.23,23.16],
    '深圳':[114.07,22.62],
    '成都':[104.06,30.67],
    '上海':[121.473701,31.230416,],
    '北京':[116.46,39.92],
    '济南':[117,36.65],
    '天津':[117.2,39.13],
    '武汉':[114.31,30.52,],
    '杭州':[120.19,30.26,]

};
var convertData = function (data) {
    var res = [];
    for (var i = 0; i < data.length; i++) {
        var geoCoord = geoCoordMap[data[i].name];
        if (geoCoord) {
            res.push({
                name: data[i].name,
                value: geoCoord.concat(data[i].value)
            });
        }
    }
    return res;
};

option = {
   // backgroundColor: '#404a59',
  /***  title: {
        text: '实时行驶车辆',
        subtext: 'data from PM25.in',
        sublink: 'http://www.pm25.in',
        left: 'center',
        textStyle: {
            color: '#fff'
        }
    },**/
    tooltip : {
        trigger: 'item',
		formatter: function (params) {
              if(typeof(params.value)[2] == "undefined"){
              	return params.name + ' : ' + params.value;
              }else{
              	return params.name + ' : ' + params.value[2];
              }
            }
    },

    geo: {   //地图设置
        map: 'china',
        label: {
            emphasis: {
                show: false
            }
        },
        roam: true,//禁止其放大缩小
        itemStyle: {
            normal: {
                areaColor: '#84dbff',      //区域里的颜色
                borderColor: '#0506cb'      //每个省的边界线颜色
            },
            emphasis: {
                areaColor: '#23d6ff'            //鼠标移到时变化的颜色
            }
        }
    },

// visualMap: {//视觉映射组件，也就是左下角的标示图
//                 top: 'center',
//                 left: 'left',
//                 min: 10000,
//                 max: 100000,
//                 text: ['High', 'Low'],
//                 realtime: false,  //拖拽时，是否实时更新
//                 calculable: true,  //是否显示拖拽用的手柄
//                 inRange: {
//                     color: ['lightskyblue', 'yellow', 'orangered']
//                 }
//             },


    series : [
        {
            name: '数量',
            type: 'scatter',
            coordinateSystem: 'geo',
            data: convertData(data),
            symbolSize: function (val) {
                return val[2] / 2500;
            },
            label: {
                normal: {  //是图形在默认状态下的样式
                    formatter: '{b}',
                    position: 'right',
                    show: false   //是否显示标签,也就是显示地图上的城市名
                },
                emphasis: {  //是图形在高亮状态下的样式,比如在鼠标悬浮或者图例联动高亮时
                    show: true
                }
            },
            itemStyle: {
                normal: {
                    color: '#fff918'
                }
            }
        }
		
		/**
		,
        {
            name: 'Top 5',
            type: 'effectScatter',
            coordinateSystem: 'geo',
            data: convertData(data.sort(function (a, b) {
                return b.value - a.value;
            }).slice(0, 6)),
            symbolSize: function (val) {
                return val[2] / 20;
            },
            showEffectOn: 'render',
            rippleEffect: {
                brushType: 'stroke'
            },
            hoverAnimation: true,
            label: {
                normal: {
                    formatter: '{b}',
                    position: 'right',
                    show: true
                }
            },
            itemStyle: {
                normal: {
                    color: '#ffd800',
                    shadowBlur: 10,
                    shadowColor: 'rgba(0,0,0,.3)'
                }
            },
            zlevel: 1
        }
		**/
    ]
};
		
        myChart.setOption(option);
        window.addEventListener("resize",function(){
            myChart.resize();
        });
    }

})

