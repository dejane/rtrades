var trades = [];

var config = {
			type: 'line',

			  legend: {
			      display: false,
                  labels: {
                    fontSize: 0
                    }
                },

			data: {
				labels: ['20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1'],
				datasets: [{
					label: 'Last orders',
					backgroundColor: window.chartColors.blue,
					borderColor: window.chartColors.blue,
					data: trades,
					fill: false,
					steppedLine: 'before',

                    		  legend: {
                        display: false,
                               labels: {
                    fontSize: 0
                }
                    },
				}]
			},
			options: {
				responsive: true,
				title: {
					display: false,
					text: 'Last orders'
				},
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Last orders'
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Price'
						}
					}]
				}
			}
		};
