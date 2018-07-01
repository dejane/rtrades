$(document).ready(function(){

        var all = $(".btc_price").map(function() {
            return this.innerHTML;
        }).get();

        var vsi = all.join();
        vsi = vsi.split(',');

        for(i = 0; i < vsi.length; i++) {

            if(i < 20) {
              trades.push(parseFloat(vsi[i]));
              }

            }

			var ctx = document.getElementById('canvas').getContext('2d');
			window.myLine = new Chart(ctx, config);

  });