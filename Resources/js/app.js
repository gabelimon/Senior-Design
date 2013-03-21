function logMyErrors(e) {
  console.log(e);
}

$(document).ready(function () {
    try {
      var window = Ti.UI.currentWindow;
      window.maximize();
    }
    catch (e) {
      // statements to handle any exceptions
      logMyErrors(e); // pass exception object to error handler
    }
    var userName = "";
    currentManifest = []; // Global manifest variable
    steps = []; // A global array of steps to finish
    // Here we should force a log on
    //console.log("continuing");


    //Untested. Probably works

    function applyManifest(manifest) {
        console.log("attempting to apply manifest");
        console.log(Object.keys(manifest) +',' + manifest["A"].length);
        var k = Object.keys(manifest); // These are the keys. I named them keys
                                       // but that blew up because of conflicts
        // There are currently bugs here. I'm getting an undefined object error
        // as I iterate
        for (var i = 0; i < k.length; i++) {
            for (var j = 0; j < 6; j++) {
                $("#teus-inner"+" #row" + j +" ." + k[i]+" a").html(
                manifest[k[i]][j] !== unoccupied 
                ?(manifest[k[i]][j].substr(0, 5) + ".."):"(empty)");
            }
        }
    }

    $("#uploadManifestSubmit").click(function () {
        //console.log("It's being called");
        var textManifest = $("#manifestBody").val();
        if (textManifest === "") return;
        steps = [];

        currentManifest = format_manifest(textManifest);
        //console.log(currentManifest);
        $("#manifestDismiss").click();
        //console.log("attempted to close manifest loader");
        applyManifest(currentManifest);
    });

    // Populate the list of users
    $("#ch-user-btn").click(function () {
        try {
          userf = Ti.Filesystem.getFile(Ti.Filesystem.getApplicationDataDirectory(), 'users.txt');
          users = Ti.Filesystem.getFileStream(Ti.Filesystem.getApplicationDataDirectory(), 'users.txt');
          names = [];
          if (!userf.exists()) {
              users.open(Ti.Filesystem.MODE_WRITE);
              tests = ["1,John",
                      "2,Keogh",
                      "3,Steve"
              ];
              for (var i = 0; i < tests.length; i++) {
                 users.write(tests[i] + '\n');
              }
              users.close();
          }
          //line;
          users.open(Ti.Filesystem.MODE_READ);
          line = users.readLine();
          do {
              names.push(line.split(','));
              line = users.readLine();
          }
          while (line !== null);
          users.close();

          for (var i = 0; i < names.length; i++) {
              if( names[i]==="" ) break;
              var id = names[i][0]
              var name = names[i][1];
              $("#userForm").prepend('<label class="radio"><input type="radio" ' +
                  ' name="userName" id="userID-' +
                  id + '" value="' +
                  name + '">' + name + '</label>');
         }
      }
      catch (e) {
        // statements to handle any exceptions
        logMyErrors(e); // pass exception object to error handler
      }
    });
});
