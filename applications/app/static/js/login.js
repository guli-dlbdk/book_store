var app = new Vue({
  'el': '#login-app',
  'data': {
      'name': '',
      'passwd': ''
  },
  'methods': {
    'loginOnclick': function () {
      data = JSON.stringify({'name': this.name, 'passwd': this.passwd});
      resp = request('POST', 'api/auth', [['Content-Type', 'application/json']], data);
      resp = JSON.parse(resp);
      if (resp.status == 'OK') {
        setTimeout(function(){document.location.href = '/';}, 10)
        document.write(window.location.href);
      } else {
        alert('Kullanıcı adı ya da şifre hatalı ');
      }
    },
    'saveRegister': function () {
      data = JSON.stringify({'name': this.name, 'passwd': this.passwd});
      resp = request('POST', 'api/user', [['Content-Type', 'application/json']], data);
      resp = JSON.parse(resp);
      if (resp.status == 'OK') {
        setTimeout(function(){document.location.href = '/login';}, 10)
        document.write(window.location.href);
      } else {
        alert('Kullanıcı oluşturulamadı ');
      }
    }
  }
});