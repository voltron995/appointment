<script
  src="https://code.jquery.com/jquery-3.2.1.min.js"
  integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
  crossorigin="anonymous">
</script>

<script>
  $( document ).ready(function() {
    var map = {
      "ad": "g",
      "be": "h",
      "cf": "i"
    };

    $("#form input[name='group1'], #form input[name='group2']").on("change", function() {
      var value1 = $("#form input[name='group1']:checked").val();
      var value2 = $("#form input[name='group2']:checked").val();

      if(value1 && value2) {
        var result = value1 + value2;
        $("#form input[value=" + map[result] + "]").prop('checked',true);
      }
    })
  });
</script>

<body>

<form id="form">
  <input type="radio" name="group1" value="a" /> a
  <input type="radio" name="group1" value="b" /> b
  <input type="radio" name="group1" value="c" /> c
  <br/>
  <input type="radio" name="group2" value="d" /> d
  <input type="radio" name="group2" value="e" /> e
  <input type="radio" name="group2" value="f" /> f
  <br/>
  <input type="radio" name="group3" value="g" /> g
  <input type="radio" name="group3" value="h" /> h
  <input type="radio" name="group3" value="i" /> i
</form>

</body>