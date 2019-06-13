$(document).ready(function(){

  var loggify = function(){
    $(".response-wrapper").remove();
    $(".task").each(function(ii){
    var whatever = `<span class="response-wrapper"><span class="expansive-button">
           Toggle here to answer: <i class="fa fa-pencil-square-o" data-task-id="${ii}"></i>
        </span>
        <textarea class="hidden student-response" placeholder="Give your answer or make notes to yourself" data-response-id="${ii}"></textarea>
        </span>`;
      $(this).append(whatever);
      var jj = ii.toString();
      thesenotes.child(jj).on("value", function(snap){
        var myanswers = snap.val();
        $(`textarea[data-response-id=${jj}]`).val(myanswers);
      });
    });

    $(".expansive-button").click(function(evt){
      var targetid = $(evt.currentTarget).find("i").data("taskId");
        $(`[data-response-id=${targetid}]`).toggleClass("hidden");
    });
    $(".student-response").blur(function(evt){
      var thedata = $(evt.currentTarget).val();
      var taskid = $(evt.currentTarget).data("responseId");
      thesenotes.child(taskid).set(thedata);
    });
  };

// Initialize Firebase
var config = {
  apiKey: "AIzaSyDpd8z9ASaZBHSnqdP0GjgHSNqnhujJ-7Y",
  authDomain: "profninjanotes.firebaseapp.com",
  databaseURL: "https://profninjanotes.firebaseio.com",
  projectId: "profninjanotes",
  storageBucket: "profninjanotes.appspot.com",
  messagingSenderId: "363402967891"
};
firebase.initializeApp(config);

var provider = new firebase.auth.GithubAuthProvider();

$("#login").click(function(){
  firebase.auth().signInWithRedirect(provider);
});

$("#logout").click(function(){
  firebase.auth().signOut();
});

var showLogin = function(){
  $("#login_part").show();
  $("#logout_part").hide();
};

var showLogout = function(){
  $("#login_part").hide();
  $("#logout_part").show();
};

var encodeKey = function(s) { return encodeURIComponent(s.replace(/\//g,'-')).replace(/\./g, '%2E'); };

var thesenotes = null;

var userhandle = function(user){
  if (user){
    thisperson = user.email;
    $(".username").html(user.email);
    thesenotes = firebase.database().ref(courseid).child(encodeKey(window.location.pathname)).child(user.uid);
    firebase.database().ref(courseid).child("users").child(user.uid).set(encodeKey(user.email));
    loggify();
    showLogout();
  } else {
    showLogin();
    $(".expansive-button").addClass("hidden");
  }
}

firebase.auth().onAuthStateChanged(userhandle);

firebase.auth().getRedirectResult().then(function(result) {
  var user = result.user;
  userhandle(user);
});

});
