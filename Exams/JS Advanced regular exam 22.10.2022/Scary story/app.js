window.addEventListener("load", solve);

function solve() {
    document.getElementById('form-btn').addEventListener('click', publishStory);
    let firstName = document.getElementById('first-name');
    let lastName = document.getElementById('last-name');
    let age = document.getElementById('age');
    let storyTitle = document.getElementById('story-title');
    let genre = document.getElementById('genre');
    let storyText = document.getElementById('story');
    let previewSection = document.getElementById('preview-list');
    let mainSection = document.getElementById('main');


    function publishStory(event) {
      event.preventDefault();

      let firstNameValue = firstName.value;
      let lastNameValue = lastName.value;
      let ageValue = age.value;
      let storyTitleValue = storyTitle.value;
      let genreValue = genre.value;
      let storyTextValue = storyText.value;

      if (!firstNameValue || !lastNameValue || !ageValue || !storyTitleValue || !storyTextValue) {
        return;
      };

      createDOMElements(firstNameValue, lastNameValue, ageValue, storyTitleValue, genreValue, storyTextValue);
      clearForm();
    };

    function clearForm() {
      firstName.value = "";
      lastName.value = "";
      age.value = "";
      storyTitle.value = "";
      genre.value = "Disturbing";
      storyText.value = "";
      let publishButton = document.getElementById('form-btn')
      publishButton.setAttribute('disabled', true);
    };

    function createDOMElements(firstNameValue, lastNameValue, ageValue, storyTitleValue, genreValue, storyTextValue) {
      let li = document.createElement('li');
      li.setAttribute('class', 'story-info');

      let article = document.createElement('article');

      let h4 = document.createElement('h4');
      h4.textContent = `Name: ${firstNameValue} ${lastNameValue}`;

      let p1 = document.createElement('p');
      p1.textContent = `Age: ${ageValue}`;
      let p2 = document.createElement('p');
      p2.textContent = `Title: ${storyTitleValue}`;
      let p3 = document.createElement('p');
      p3.textContent = `Genre: ${genreValue}`;
      let p4 = document.createElement('p');
      p4.textContent = `${storyTextValue}`;

      let saveBtn = document.createElement('button');
      saveBtn.setAttribute('class', 'save-btn');
      saveBtn.textContent = 'Save Story';
      saveBtn.addEventListener('click', saveStory);

      let editBtn = document.createElement('button');
      editBtn.setAttribute('class', 'edit-btn');
      editBtn.textContent = 'Edit Story';
      editBtn.addEventListener('click', editStory);

      let deleteBtn = document.createElement('button');
      deleteBtn.setAttribute('class', 'delete-btn');
      deleteBtn.textContent = 'Delete Story';
      deleteBtn.addEventListener('click', deleteStory);

      article.appendChild(h4);
      article.appendChild(p1);
      article.appendChild(p2);
      article.appendChild(p3);
      article.appendChild(p4);

      li.appendChild(article);
      li.appendChild(saveBtn);
      li.appendChild(editBtn);
      li.appendChild(deleteBtn);

      previewSection.appendChild(li);
    };

      function editStory(event) {
        event.preventDefault();

        let info = event.target.parentElement;
        firstName.value = info.children[0].children[0].textContent.split(': ')[1].split(' ')[0];
        lastName.value = info.children[0].children[0].textContent.split(': ')[1].split(' ')[1];
        age.value = Number(info.children[0].children[1].textContent.split(': ')[1]);
        storyTitle.value = info.children[0].children[2].textContent.split(': ')[1];
        genre.value = info.children[0].children[3].textContent.split(': ')[1];
        storyText.value = info.children[0].children[4].textContent;

        info.parentElement.removeChild(info); 

        let publishButton = document.getElementById('form-btn');
        let saveBtn = document.getElementsByClassName('save-btn');
        let editBtn = document.getElementsByClassName('edit-btn');
        let deleteBtn = document.getElementsByClassName('delete-btn');

        publishButton.disabled = false;
        saveBtn.setAttribute('disabled', true);
        editBtn.setAttribute('disabled', true);
        deleteBtn.setAttribute('disabled', true);
      };

      function saveStory(event) {
        event.preventDefault();

        let info = event.target.parentElement.parentElement.parentElement;
        info.parentElement.removeChild(info); 
        document.querySelector("#main > div").remove();
        let h1 = document.createElement('h1');
        h1.textContent = "Your scary story is saved!";
        mainSection.appendChild(h1);
      };

      function deleteStory(event) {
        event.preventDefault();
        let info = event.target.parentElement.parentElement;
        info.parentElement.removeChild(info); 

        let publishButton = document.getElementById('form-btn');
        publishButton.disabled = false;
        
      };
  };