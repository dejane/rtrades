
function showBtc() {
  $("#tbody1").css("display", "table-row-group");
  $("#tbody2").css("display", "none");
  $("#tbody3").css("display", "none");
  $("#link1").addClass("active");
  $("#link2").removeClass("active");
  $("#link3").removeClass("active");


  var all = $(".btc_price").map(function() {
      return this.innerHTML;
  }).get();

  var vsi = all.join();
  vsi = vsi.split(',');
  trades = [];

  for(i = 0; i < vsi.length; i++) {
      if(i < 21) {
          trades.push(parseFloat(vsi[i]));
      }

  }
  config.data.datasets[0].data = trades;
  window.myLine.update();

}

function showEth() {
  $("#tbody1").css("display", "none");
  $("#tbody2").css("display", "table-row-group");
  $("#tbody3").css("display", "none");
  $("#link2").addClass("active");
  $("#link1").removeClass("active");
  $("#link3").removeClass("active");

  var all = $(".eth_price").map(function() {
      return this.innerHTML;
  }).get();

  var vsi = all.join();
  vsi = vsi.split(',');
  trades = [];

  for(i = 0; i < vsi.length; i++) {
      if(i < 21) {
          trades.push(parseFloat(vsi[i]));
      }

  }
  config.data.datasets[0].data = trades;
  window.myLine.update();

}

function showXrp() {
  $("#tbody1").css("display", "none");
  $("#tbody2").css("display", "none");
  $("#tbody3").css("display", "table-row-group");
  $("#link3").addClass("active");
  $("#link1").removeClass("active");
  $("#link2").removeClass("active");

    var all = $(".xrp_price").map(function() {
      return this.innerHTML;
  }).get();

  var vsi = all.join();
  vsi = vsi.split(',');
  trades = [];

  for(i = 0; i < vsi.length; i++) {
      if(i < 21) {
          trades.push(parseFloat(vsi[i]));
      }

  }

  config.data.datasets[0].data = trades;
  window.myLine.update();

}
  //function for time conversion -->

function convTime(ob){
    var date = new Date(parseInt(ob)*1000);
    var day = date.getDate();
    var month = date.getMonth();
    var year = date.getFullYear();
    var hours = date.getHours();
    var minutes = "0" + date.getMinutes();
    var seconds = "0" + date.getSeconds();
    var finTime = day+'.'+month+'.'+year+'   '+hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
    return finTime;
  }

//for BTC
  $(document).ready(function(){

    $("td[id*='tms']").each(function(){
      ct = $(this).html()
      var res = convTime(ct)
      $(this).html(res)
    });
    setInterval(function(){
      var elm = $("#tbody1 tr").first().children().first().html();
      $.get("http://localhost:5000/api/update/btcusd/"+ elm, function(data){
        if (data.updates == "No updates"){
          return 0;
        }else if(data.size >= 1){
          var v = data.updates
          for(x of v){
            $("#tbody1 tr").last().remove();
            $("#tbody1").prepend("<tr><td style='display:none;'>"+x['id']+"</td><td>"+ convTime(x['timestamp']) +"</td><td>"+x['price']+"</td></tr>");

            if($("#link1").hasClass("active")) {
                        config.data.datasets.forEach(function(dataset) {
                            dataset.data.splice(0, 1); // remove first data point
                        });
                        window.myLine.update();

                        config.data.datasets.forEach(function(dataset, index) {
                            dataset.data.push(parseFloat(x['price'])); // add new data at end
                        });
                        window.myLine.update();
            }

          }

        }else{
          console.log('Uncaught error')
        }
      }, "json"
    );

    }, 3000);


  });

//for eth
  $(document).ready(function(){

    /*$("td[id*='tms2']").each(function(){
      ct2 = $(this).html()
      console.log(ct2)
      $(this).html(convTime(ct2))
    });*/
    setInterval(function(){
      var elm = $("#tbody2 tr").first().children().first().html();
      $.get("http://localhost:5000/api/update/ethusd/"+ elm, function(data){
        if (data.updates == "No updates"){
          return 0;
        }else if(data.size >= 1){
          var v = data.updates
          for(x of v){
            $("#tbody2 tr").last().remove();
            $("#tbody2").prepend("<tr><td style='display:none;'>"+x['id']+"</td><td>"+ convTime(x['timestamp'])+"</td><td>"+x['price']+"</td></tr>");

                        if($("#link2").hasClass("active")) {
                        config.data.datasets.forEach(function(dataset) {
                            dataset.data.splice(0, 1); // remove first data point
                        });
                        window.myLine.update();

                        config.data.datasets.forEach(function(dataset, index) {
                            dataset.data.push(parseFloat(x['price'])); // add new data at end
                        });
                        window.myLine.update();
            }

          }

        }else{
          console.log('Uncaught error')
        }
      }, "json"
    );

    }, 3000);


  });

    $(document).ready(function(){

      /*$("td[id*='tms3']").each(function(){
        ct = $(this).html()
        var res = convTime(ct)
        $(this).html(res)
      });*/
      setInterval(function(){
        var elm = $("#tbody3 tr").first().children().first().html();
        $.get("http://localhost:5000/api/update/xrpusd/"+ elm, function(data){
          if (data.updates == "No updates"){
            return 0;
          }else if(data.size >= 1){
            var v = data.updates
            for(x of v){
              $("#tbody3 tr").last().remove();
              $("#tbody3").prepend("<tr><td style='display:none;'>"+x['id']+"</td><td>"+ convTime(x['timestamp'])+"</td><td>"+x['price']+"</td></tr>");

                          if($("#link3").hasClass("active")) {
                        config.data.datasets.forEach(function(dataset) {
                            dataset.data.splice(0, 1); // remove first data point
                        });
                        window.myLine.update();

                        config.data.datasets.forEach(function(dataset, index) {
                            dataset.data.push(parseFloat(x['price'])); // add new data at end
                        });
                        window.myLine.update();
            }

            }

          }else{
            console.log('Uncaught error')
          }
        }, "json"
      );

      }, 3000);

    });
