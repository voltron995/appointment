  $( document ).ready(function() {
    var radio_time_data = $("#radio_form .radio_time input").map(function() {
       return [[
         $(this).val(), 
         $(this).attr("data-date-id") 
       ]];                                     
    });
       
    var radio_date_time_map = _(radio_time_data)
      .groupBy(function(e) { return e[1]; })
      .mapValues(function(v) { return v.map(function(e) { return e[0]; }) })
      .value();
   
        
    var resetTimeInputs = function() {
      $("#id_time_ranges").val("");
      $("#radio_form input[name=times]").prop("checked", false);
      $("#radio_form .radio_time").each(function() { $(this).hide(); });
    };
    
    var showTimeInputs = function(time_radios_to_show) {
      $("#radio_form .radio_time").each(function() {
        var current_radio_div = $(this);
        $(this).find("input[type=radio]").each(function() {
          if(_.includes(time_radios_to_show, $(this).val())) {
            current_radio_div.show();
          };
        });
      });
    };
    
    var switch_time_radios = function() {
      var checked_date_id = $("#radio_form input[name='dates']:checked").val();
      var time_radios_to_show = radio_date_time_map[checked_date_id];
      
      resetTimeInputs();
      showTimeInputs(time_radios_to_show);
    };
    
    var set_time_range = function() {
      var date_id = $("#radio_form input[name='dates']:checked").val();
      var time_id = $("#radio_form input[name='times']:checked").val();
      if(date_id && time_id) {
        $("#id_time_ranges").val(time_id);
      }
    };

    var setAppointmentsId = function() {
        $("#id_appointments").val($("#id_appointments option:eq(1)").val());
    };

    var hideFields = function(){
    $('#id_time_ranges').hide();
    $('#id_appointments').hide();
    // and then the on-click stuff...
    };

    resetTimeInputs();
    
    $("#radio_form input[name='dates']")
      .on("change", function() { switch_time_radios(); });

    $("#radio_form input[name='times']")
      .on("change", function() { set_time_range(); });

    setAppointmentsId();

    hideFields();

  });
