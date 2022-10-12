console.log("Welcome");
window.addEventListener("load", function() {
  showJournal();
  let addBtn = document.getElementById("addBtn");
  addBtn.addEventListener("click", addJournal);
})

// If user adds a journal, add it to the localStorage

function addJournal() {
  let addTxt = document.getElementById("addTxt");
  let addTitle = document.getElementById("addTitle");
  let journals = localStorage.getItem("journals");
  if (journals == null) {
    journalsObj = [];
  } else {
    journalsObj = JSON.parse(journals);
  }
  let myObj = {
    title: addTitle.value,
    text: addTxt.value
  }
  journalsObj.push(myObj);
  localStorage.setItem("journals", JSON.stringify(journalsObj));
  addTxt.value = "";
  addTitle.value = "";
  showJournal();
}

// Function to show elements from localStorage
function showJournal() {
  let journals = localStorage.getItem("journals");
  // journals = {
  //     "entries" : [
  //       {
  //       "title" : "my title",
  //       "body" : "sfhssdf"
  //     }
  //   ]
  // }

  if (journals == null) {
    journalsObj = [];
  } else {
    journalsObj = JSON.parse(journals);
  }
  console.log(journalsObj);
  let html = "";
  journalsObj.forEach(function(element, index) {
    html += `
            <div class="journalCard my-2 mx-2 card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">${element.title}</h5>
                        <p class="card-text"> ${element.text}</p>
                        <button id="${index}"onclick="deleteJournal(this.id)" class="btn btn-primary">Delete Journal</button>
                    </div>
                </div>`;
  });
  let journalsElm = document.getElementById("journals");
  //console.log(journalsElm)
  if (journalsObj.length != 0) {
    journalsElm.innerHTML = html;
  } else {
    journalsElm.innerHTML = `Nothing to show! Use "Add a journal" section above to add journals.`;
  }
}

// Function to delete a journal
function deleteJournal(index) {

  let journals = localStorage.getItem("journals");
  if (journals == null) {
    journalsObj = [];
  } else {
    journalsObj = JSON.parse(journals);
  }

  journalsObj.splice(index, 1);
  localStorage.setItem("journals", JSON.stringify(journalsObj));
  showJournal();
}


// let search = document.getElementById('searchTxt');
// search.addEventListener("input", function(){

//     let inputVal = search.value.toLowerCase();

//     let journalCards = document.getElementsByClassName('journalCard');
//     Array.from(journalCards).forEach(function(element){
//         let cardTxt = element.getElementsByTagName("p")[0].innerText;
//         if(cardTxt.includes(inputVal)){
//             element.style.display = "block";
//         }
//         else{
//             element.style.display = "none";
//         }

//     })
// })
