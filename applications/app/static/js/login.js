var loginapp = new Vue({
  el: "#login-app",
  data: {
    name: "",
    passwd: "",
    currentUser: null,
    profileUser: {}
  },
  mounted: function () {
    if (localStorage.currentUser) {
      this.currentUser = JSON.parse(localStorage.currentUser);
    }
    this.profileUser = this.getUserFromParams()
  },
  methods: {
    loginOnclick: function () {
      data = JSON.stringify({ name: this.name, passwd: this.passwd });
      resp = request(
        "POST",
        "api/auth",
        [["Content-Type", "application/json"]],
        data
      );
      resp = JSON.parse(resp);
      if (resp.status == "OK") {
        localStorage.currentUser = resp.data[0] && JSON.stringify(resp.data[0]);
        setTimeout(function () {
          document.location.href = "/";
        }, 10);
        document.write(window.location.href);
      } else {
        this.name = ''
        this.passwd = ''
        alert("Kullanıcı adı ya da şifre hatalı ");
      }
    },
    saveRegister: function () {
      data = JSON.stringify({ name: this.name, passwd: this.passwd });
      resp = request(
        "POST",
        "api/user",
        [["Content-Type", "application/json"]],
        data
      );
      resp = JSON.parse(resp);
      if (resp.status == "OK") {
        setTimeout(function () {
          document.location.href = "/login";
        }, 10);
        document.write(window.location.href);
        this.name = ''
        this.passwd = ''
      } else {
        alert("Kullanıcı oluşturulamadı ");
      }
    },
    logoutClick: function () {
      result = request("DELETE", "/api/auth", [], null);
      result = JSON.parse(result);
      if (result.status == "OK") {
        location.reload();
        localStorage.removeItem("currentUser")
        this.currentUser = null
      }
    },
    getUserFromParams: function () {
      let uri = window.location.search.substring(1); 
      let params = new URLSearchParams(uri);
      console.log("api/user?id="+params.get("user_id"))
      result = JSON.parse(request("GET", "api/user?id="+params.get("user_id") , [], null));
      return result.data[0]
    },
    changeUserRole: function(userId, role) {
      data = JSON.stringify({ 'role': role})
      console.log('data', userId,role)
      resp = request(
        "PUT",
        "api/user?id="+userId,
        [["Content-Type", "application/json"]],data);
      result = JSON.parse(resp);
      if (result.status == "OK") {
        this.profileUser = this.getUserFromParams()
        alert("user is now "+role);
      } else {
        alert("user couldn't be made "+role);
      }
    }
  },
});

