function logMyErrors(e) {
  console.log(e);
}

$(document).ready(function () {
    try {
      var window = Ti.UI.currentWindow;
      window.maximize();
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

    } catch (e) {
        // statements to handle any exceptions
        console.log("ERROR ERROR: "+e); // pass exception object to error handler



    // statements to handle any exceptions


=======
=======
>>>>>>> parent of 3c6051c... updating
=======
>>>>>>> parent of 3c6051c... updating
    }
    catch (e) {
      // statements to handle any exceptions
      logMyErrors(e); // pass exception object to error handler
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> parent of 3c6051c... updating
=======
>>>>>>> parent of 3c6051c... updating
=======
>>>>>>> parent of 3c6051c... updating
    }
    var userName = "";
    currentManifest = []; // Global manifest variable
    steps = []; // A global array of steps to finish
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

    
    // We should create the log file if it's not there
    try {
        var logf = Ti.Filesystem.getFile(Ti.Filesystem.getApplicationDataDirectory(), 'logs.txt');
        var logs = Ti.Filesystem.getFileStream(Ti.Filesystem.getApplicationDataDirectory(), 'logs.txt');
        if (!logf.exists()) {
            logs.open(Ti.Filesystem.MODE_WRITE);
            logs.write("CREATED "+Date());
            logs.close();
        }
    } catch(e) {
    // statements to handle any exceptions
        console.log("ERROR ERROR: "+e); // pass exception object to error handler
    }  
    


    // Here we should force a log on
    //console.log("continuing");



    // Copies manifest to clipboard
    $("#copyBtn").click(function() {
        window.clipboardData.setData("Text", $("#manifestDump").html());
    });


    // enable removal
    $("#teus-inner a").click(function() {
        if( $(this).hasClass('disabled') ) return;
        if( $(this).hasClass('btn-success') ){
            $(this).removeClass('btn-success');
            $('#addTEUbtn').removeClass('disabled');
            $('#removeTEUbtn').addClass('disabled');
            return;
        }
        $("#teus-inner .btn-success").removeClass("btn-success");
        $(this).addClass("btn-success");
        $(this).addClass("selected-teu");
        $('#addTEUbtn').addClass('disabled');
        $('#removeTEUbtn').removeClass('disabled');
    });


    // WORKING HERE
    // This part actually generates the steps
    $("#removeTEU").click( function() {
        if( $(this).hasClass('disabled') ) return;
        var col = $(this).parent().replace(" span1 teu", ""); //gets column
        var row = parseInt($(this).parent$().parent().attr("id").replace('row','')); //gets row
        steps = remove_boxes( currentManifest, [col,row] );
    });

    // Dumps out the buffer
    $("#viewBufbtn").click(function() {
        var bufferContents = "";
        for( var i = 0; i < currentManifest['buffer'].length; i++ ) {
            bufferContents = "<p>"+currentManifest['buffer']+"</p>";
        }
        $("#bufferDump").html(bufferContents);
    });

    // Throws the manifest onto the screen

    //Untested. Probably works


=======
    // Here we should force a log on
    //console.log("continuing");


    //Untested. Probably works

>>>>>>> parent of 3c6051c... updating
=======
    // Here we should force a log on
    //console.log("continuing");


    //Untested. Probably works

>>>>>>> parent of 3c6051c... updating
=======
    // Here we should force a log on
    //console.log("continuing");


    //Untested. Probably works

>>>>>>> parent of 3c6051c... updating
    function applyManifest(manifest) {
        console.log("attempting to apply manifest");
        console.log(Object.keys(manifest) +',' + manifest["A"].length);
        var k = Object.keys(manifest); // These are the keys. I named them keys
                                       // but that blew up because of conflicts
        // There are currently bugs here. I'm getting an undefined object error
        // as I iterate
        for (var i = 0; i < k.length; i++) {
            for (var j = 0; j < 6; j++) {
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

                if(manifest[k[i]][j] !== unoccupied) {
                    //console.log("attempting to write to: "+ "#teus-inner #row" + j+1 +" ." + k[i]+" a");
                    $("#teus-inner #row" + (j+1) +" ." + k[i]+" a").html( 
                    manifest[k[i]][j].substr(0, 5) + "..")
                    .removeClass("disabled");
                }
                else {
                    $("#teus-inner #row" + (j+1) +" ." + k[i]+" a")
                    .html("(empty)").addClass("disabled");






=======
                $("#teus-inner"+" #row" + j +" ." + k[i]+" a").html(
                manifest[k[i]][j] !== unoccupied 
                ?(manifest[k[i]][j].substr(0, 5) + ".."):"(empty)");
>>>>>>> parent of 3c6051c... updating
=======
                $("#teus-inner"+" #row" + j +" ." + k[i]+" a").html(
                manifest[k[i]][j] !== unoccupied 
                ?(manifest[k[i]][j].substr(0, 5) + ".."):"(empty)");
>>>>>>> parent of 3c6051c... updating
=======
                $("#teus-inner"+" #row" + j +" ." + k[i]+" a").html(
                manifest[k[i]][j] !== unoccupied 
                ?(manifest[k[i]][j].substr(0, 5) + ".."):"(empty)");
>>>>>>> parent of 3c6051c... updating
            }
        }
    }

    $("#uploadManifestSubmit").click(function () {
        //console.log("It's being called");
        var textManifest = $("#manifestBody").val();
        if (textManifest === "") return;
        currentManifest = format_manifest(textManifest);
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

       //console.log("MANIFEST FORMATTED");

        //console.log(currentManifest);

=======
        //console.log(currentManifest);
>>>>>>> parent of 3c6051c... updating
=======
        //console.log(currentManifest);
>>>>>>> parent of 3c6051c... updating
=======
        //console.log(currentManifest);
>>>>>>> parent of 3c6051c... updating
        $("#manifestDismiss").click();
        //console.log("attempted to close manifest loader");
        applyManifest(currentManifest);
    });
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

    
    // Display log history
   $('#viewLogbtn').click(function() {
        try {
          var logs = Ti.Filesystem.getFileStream(Ti.Filesystem.getApplicationDataDirectory(), 'logs.txt');
          logs.open(Ti.Filesystem.MODE_READ);
          var line = logs.readLine();
          logStr = "";
          do {
              logStr += line;
              line = "<p>"+logs.readLine()+"</p>";
          }
          while (line !== null);
          logs.close();
          $("#logSpace").html(logStr);
        } catch (e) {
           // statements to handle any exceptions
           console.log("error: "+e); // pass exception object to error handler
        }
    });
=======
>>>>>>> parent of 3c6051c... updating


=======
>>>>>>> parent of 3c6051c... updating
=======
>>>>>>> parent of 3c6051c... updating

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
      } catch (e) {
        // statements to handle any exceptions
        logMyErrors(e); // pass exception object to error handler
      }
    });
});
