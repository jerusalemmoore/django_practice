
  $(document).ready( function() {
    // i have to double json.parse in order to deal with over stringified json element
    // https://stackoverflow.com/questions/42494823/json-parse-returns-string-instead-of-object
    const list = JSON.parse(JSON.parse(document.getElementById("usersList").textContent))
    const listUsernames = []
    for (let i = 0; i < list.length; i++){
      // console.log("hello")
      listUsernames.push(list[i].fields.username)
      
    }
    // console.log(listUsernames)
    // var availableTags = [{% for user in users %}"{{user.username}}",{% endfor %}];
    $( "#tags" ).autocomplete({
      source: listUsernames,
      minLength:2,
      select: function(event, ui){
        $("#tags").val(ui.item.label);
        $("#myform").submit();
      }
    });
    });

    