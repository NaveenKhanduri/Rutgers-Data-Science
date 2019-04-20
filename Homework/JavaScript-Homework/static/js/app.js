// from data.js
var tableData = data;

// YOUR CODE HERE!
function addrow(i){
        
        var tableRef = document.getElementById("ufo-table")//.getElementsByTagName('tbody')[0];
        var newRow = tableRef.insertRow(-1);

        var dateCell = newRow.insertCell(0);
        dateCell.innerHTML = i.datetime;

        let citycell = newRow.insertCell(1);
        citycell.innerHTML = i.city;

         let statecell = newRow.insertCell(2); 
        statecell.innerHTML = i.state;

        let countrycell = newRow.insertCell(3);
        countrycell.innerHTML = i.country;

        let shapecell = newRow.insertCell(4);
         shapecell.innerHTML = i.shape;

        let duracell = newRow.insertCell(5);
        duracell.innerHTML = i.durationMinutes;

        let commentcell = newRow.insertCell(6);
        commentcell.innerHTML = i.comments;  
}

function dateFunction() {

        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("filterInput");
        filter = input.value;
        table = document.getElementById("ufo-table");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
          td = tr[i].getElementsByTagName("td")[0];
          if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.indexOf(filter) > -1) {
              tr[i].style.display = "";
            } else {
              tr[i].style.display = "none";
            }
          }       
        }
      }
function shapeFunction(){

        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("filterInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("ufo-table");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[4];
                if (td) {
                  txtValue = td.textContent || td.innerText;
                  if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                  } else {
                    tr[i].style.display = "none";
                  }
                }       
              }

}
function cityFunction(){
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("filterInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("ufo-table");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[1];
                if (td) {
                  txtValue = td.textContent || td.innerText;
                  if (txtValue.durationFunction.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                  } else {
                    tr[i].style.display = "none";
                  }
                }       
              }
}

function stateFunction(){
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("filterInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("ufo-table");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[2];
                if (td) {
                  txtValue = td.textContent || td.innerText;
                  if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                  } else {
                    tr[i].style.display = "none";
                  }
                }       
              }
}

function countryFunction(){
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("filterInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("ufo-table");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[3];
                if (td) {
                  txtValue = td.textContent || td.innerText;
                  if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                  } else {
                    tr[i].style.display = "none";
                  }
                }       
              }
}

function durationFunction(){
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("filterInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("ufo-table");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[5];
                if (td) {
                  txtValue = td.textContent || td.innerText;
                  if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                  } else {
                    tr[i].style.display = "none";
                  }
                }       
              }
}
function commentsFunction(){
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("filterInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("ufo-table");
        tr = table.getElementsByTagName("tr");
        for (i = 0; i < tr.length; i++) {
                td = tr[i].getElementsByTagName("td")[6];
                if (td) {
                  txtValue = td.textContent || td.innerText;
                  if (txtValue.indexOf(filter) > -1) {
                    tr[i].style.display = "";
                  } else {
                    tr[i].style.display = "none";
                  }
                }       
              }
}
function dateSwap(){
        var dateSearch = '<label for="dateCell">Enter a Date</label> <input class="form-control" id="filterInput" onkeyup = "dateFunction()" type="text" placeholder="1/11/2011"> </input>';
        document.getElementById("filterSet").innerHTML = dateSearch;

}
function shapeSwap(){
        var shapeSearch = '<label for="shapeCell">Enter a Shape</label> <input class="form-control" id="filterInput" onkeyup = "shapeFunction()" type="text" placeholder="shape"> </input>';
        document.getElementById("filterSet").innerHTML = shapeSearch;
}
function citySwap(){
        var citySearch = '<label for="dateCell">Enter a City</label> <input class="form-control" id="filterInput" onkeyup = "cityFunction()" type="text" placeholder="City"> </input>';
        document.getElementById("filterSet").innerHTML = citySearch;
}
function stateSwap(){
        var stateSearch = '<label for="dateCell">Enter a State</label> <input class="form-control" id="filterInput" onkeyup = "stateFunction()" type="text" placeholder="State"> </input>';
        document.getElementById("filterSet").innerHTML = stateSearch;
}
function countrySwap(){
        var countrySearch = '<label for="dateCell">Enter a Country</label> <input class="form-control" id="filterInput" onkeyup = "countryFunction()" type="text" placeholder="Country"> </input>';
        document.getElementById("filterSet").innerHTML = countrySearch;
}
function durationSwap(){
        var durSearch = '<label for="dateCell">Enter a duration time</label> <input class="form-control" id="filterInput" onkeyup = "durationFunction()" type="text" placeholder="City"> </input>';
        document.getElementById("filterSet").innerHTML = durSearch;
}
function commentSwap(){
        var commentSearch = '<label for="dateCell">Enter a Comment</label> <input class="form-control" id="filterInput" onkeyup = "commentsFunction()" type="text" placeholder="City"> </input>';
        document.getElementById("filterSet").innerHTML = commentSearch;
}