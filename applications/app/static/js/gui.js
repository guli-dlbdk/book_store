Vue.component("book_item", {
  props: ["book"],
  template: `
    <transition name="book-item">
      <div>
        <div class="col d-flex align-items-start">
        <div class="icon-square bg-light text-dark flex-shrink-0 me-3" style="background-color: #dceeff!important;margin-right:16px;">
          <i class="bi bi-journal-album" style="font-size: 2rem; color: black;"></i>
        </div>
        <div style="margin-bottom:30px;">
          <h2>{{book.name}}</h2>
          <span>
            <h5 style="color:#8b97e0"><i class="bi bi-person-bounding-box" style="font-size: 1rem; margin-right:5px;"></i>
            {{book.author}}</h5>
          </span>
          <p>{{book.description}}</p>
          <slot name="footer"></slot>
        </div>
      </div>
      </div>
    </transition>
  `,
  methods: {
    
  },
});

var app = new Vue({
  el: "#app",
  data: {
    books: [],
    searchText: '',
    book: {
      id: null,
      name: '',
      author:'',
      description: ''
    },
    selectedBook: '',
    currentUser: null,
    users: [],
    message: ''
  },
  mounted: function () {
    if (localStorage.currentUser) {
      this.currentUser = JSON.parse(localStorage.currentUser);
    }
    this.getBook()
    this.getUser()
  },
  methods: {
    searchBooks: function(){
      async_request("GET", "api/book?text="+this.searchText , [], null, this.bookCallback);
    },
    bookCallback: function (response) {
      result = JSON.parse(response);
      if (result.status == "OK") {
        this.books = result.data
      } else {
        alert('Hata')
      }
    },
    getBook: function() {
      async_request("GET", "api/book" , [], null, this.bookCallback);
    },
    userCallback: function (response) {
      result = JSON.parse(response);
      if (result.status == "OK") {
        this.users = result.data
      } else {
        alert('Hata')
      }
    },
    getUser: function () {
      resp = async_request("GET", "api/user", [], null, this.userCallback);
    },
    addBook: function () {
      data = JSON.stringify({ name: this.book.name, author: this.book.author, description: this.book.description });
      resp = request("POST", "api/book", [["Content-Type", "application/json"]], data);
      result = JSON.parse(resp);
      if (result.status == "OK") {
        this.clearData()
        this.getBook()
      } else {
        alert(result.message)
      }
    },
    deleteBook: function(item){
      res = request("DELETE", "api/book?id=" + item.id, [['Content-Type', 'application/json']], null);
      result = JSON.parse(res)
      if (result.status == 'OK') {
        this.getBook()
      } else {
        alert(result.message)
      }
    },
    editBook: function(item){
      params = JSON.stringify({ name: this.selectedBook.name, author: this.selectedBook.author, description: this.selectedBook.description });
      res = request("PUT", "api/book?id=" + item.id, [['Content-Type', 'application/json']], params);
      result = JSON.parse(res)
      if (result.status == 'OK') {
        this.getBook()
      }
    },
    clearData: function () {
      this.book = {}
    },
    logoutClick: function () {
      result = request("DELETE", "api/auth", [], null);
      result = JSON.parse(result);
      if (result.status == "OK") {
        location.reload();
      }
    }
  },
});
