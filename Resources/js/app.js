$(document).ready(function () {
    //maximize
    try {
      var window = Ti.UI.currentWindow;
      window.maximize();
    }
    catch (e) {
        // statements to handle any exceptions
        console.log("ERROR ERROR: "+e); // pass exception object to error handler
    }
    
    // Undo disabling
    $("#teus-inner a").removeClass("btn-danger");
    
    userID = 0;
    userName = "";
    users = []; // All users
    currentManifest = {}; // Global manifest variable
    steps = []; // A global array of steps to finish
    truckLabel="";
    
    // We should create the log file if it's not there
    try {
        var logf = Ti.Filesystem.getFile(Ti.Filesystem.getApplicationDataDirectory(), 'logs.txt');
        var logs = Ti.Filesystem.getFileStream(Ti.Filesystem.getApplicationDataDirectory(), 'logs.txt');
        if (!logf.exists()) {
            logs.open(Ti.Filesystem.MODE_WRITE);
            logs.write("CREATED "+Date());
            logs.close();
        }
    }
    catch(e) {
    // statements to handle any exceptions
        console.log("ERROR ERROR: "+e); // pass exception object to error handler
    }


    // TODO    
    // Here we should force a log on

    // END

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
    
    // Highlights the start and end position
    function highlightNextStep () {
        // Remove old highlighting
        $("#teus-inner a.btn-info").removeClass("btn-info");
        $("#teus-inner a.btn-warning").removeClass("btn-warning");
        $("#teus-inner a.btn-warning").removeClass("btn-warning");

        if( steps.length === 0 ) {
            $("#directions").html("Select TEU to remove");
            return;
        }
        
        var start = steps[0][0];
        var end = steps[0][1];
        // Highlight new objects
        $("#teus-inner #row" + start[1] + " ." + start[0] + " a").addClass("btn-info");
        $("#teus-inner #row" + end[1] + " ." + end[0] + " a").addClass("btn-warning");
        // Output directions
        $("#directions").html("Move " + start[0] + start[1] +
                              " to " + end[0] + end[1]);
        var selected = $("#teus-inner a.btn-success");
        if( selected.html() === "(empty)" ) selected.removeClass("btn-success");
        $("#teus-inner a").addClass("disabled");
    }
    
    // Begins the process of applying steps
    function beginSteps() {
        // disable all TEU buttons
        $("#teus-inner a").addClass("disabled");
        // enable next and cancel
        $("#cancelStepbtn,#nextStepbtn").removeClass("disabled");
        // Highlight the start and end points
        highlightNextStep();
    }
    
    function writeToLog( message ) {
        try {
            var logs = Ti.Filesystem.getFileStream(Ti.Filesystem.getApplicationDataDirectory(), 'logs.txt');
            logs.open(Ti.Filesystem.MODE_APPEND);
            logs.write(message);
            logs.close();
        }
        catch(e) {
        // statements to handle any exceptions
            console.log("ERROR ERROR: "+e); // pass exception object to error handler
        }
    }

    // WORKING HERE
    
    // Continue to next step
    // THIS SHOULD BE DONE ONCE MOVE_BOX IS UPDATED
    $("#nextStepbtn").click( function() {
        // Write to log
        var col = steps[0][0][0]; //gets column
        var row = steps[0][0][1]; //gets row
        var targetCol = steps[0][1][0]; //gets column
        var targetRow = steps[0][1][1]; //gets row
        writeToLog(userName + ": Moved " + currentManifest[col][row] +
                   " from " + col + row + " to " +
                   targetCol + targetRow + '\n');
        // Update output
        currentManifest = move_box(currentManifest, steps[0][0][0], steps[0][1][0]);

        applyManifest(currentManifest);
        steps = steps.splice(1);
        // Change highlighting
        highlightNextStep();
        var selected = $("#teus-inner a.btn-success");
        if( selected.html() === "(empty)" ) selected.removeClass("btn-success");
        if( steps.length === 0 ) {
            $("#teus-inner a").removeClass("btn-info")
                            .removeClass("btn-success")
                            .removeClass("btn-warning");
            $("#addTEUbtn").removeClass("disabled");
            $("#nextStepbtn,#cancelStepbtn").addClass("disabled");
            $("#directions").html("Select TEU to remove");
            return;
        }
        $("#teu-inner a").addClass("disabled");
    });

    // Add in TEU
    // This SHOULD be done.
    $("#addTEUbtn").click( function() {
    //    if( $(this).hasClass("disabled") ) return;
    //    currentManifest["T"][1] = $("addedTEU").val();
    //    dest = insert_box(currentManifest);
    //    steps = [[['T',1],dest]];
    //    beginSteps();
    });
    
    // Log in user
    $("#loginbtn").click( function() {
        var user = $("#userForm input [type=radio]").val();
        // Assuming they logged in remove disabling
        userName = user;
        $("#chUser button.btn").removeClass("disabled");
    });
    
    // Create new user
    $("#createUserbtn").click( function() {
    
    });
    
    // END WORK HERE
    
    // Cancel steps
    $("#cancelStepbtn").click( function() {
        var col = $("#teus-inner .btn-success").parent().attr("class").replace(" span1 teu", ""); //gets column
        var row = parseInt($("#teus-inner .btn-success").parent().parent().attr("id").replace('row','')); //gets row
        writeToLog(userName + ": Canceled removal of " + currentManifest[col][row]);
        steps = [];
        $("#teus-inner a").removeClass("btn-info")
                          .removeClass("btn-success")
                          .removeClass("btn-warning");
        $("#removeTEUbtn,#addTEUbtn").toggleClass("disabled");
        $("#cancelStepbtn,#nextStepbtn").addClass("disabled");
        // NOT OPTIMAL. I NEED TO ITERATE OVER EACH OBJECT
        applyManifest(currentManifest);
        $("#directions").html("Select TEU to remove");
    });
    
    // Removes manifest pasted in when you close the modal.
    $("#manifestDismissbtn").click( function() {
        $("#manifestBody").html("Select TEU to remove");
    });
    
    // Removes TEU
    $("#removeTEUbtn").click( function() {
        if( $(this).hasClass('disabled') ) return;
        $(this).addClass('disabled');
        var col = $("#teus-inner .btn-success").parent().attr("class").replace(" span1 teu", ""); //gets column
        var row = parseInt($("#teus-inner .btn-success").parent().parent().attr("id").replace('row','')); //gets row
        steps = remove_box( currentManifest, [col,row] );
        beginSteps();
    });

    // Dumps out the buffer
    $("#viewBufbtn").click(function() {
        var bufferContents = "";
        for( var i = 0; i < currentManifest['buffer'].length; i++ ) {
            bufferContents = "<p>"+currentManifest['buffer']+"</p>";
        }
        $("#bufferDump").html(bufferContents);
    });

    // Throws the manifest onto the screen :)
    function applyManifest(manifest) {
        var cols = ['A','B','C','D','E','F','G','H','I','H'];
        var manifestString = "";
        for( var i = 0; i < cols.length; i++ ) {
            for( var j = 0; j < manifest[cols[i]].length; j++) {
                manifestString += "<p>"+cols[i]+j+"&nbsp;"+manifest[cols[i]][j]+"</p>";
            }
        }
        $("#manifestDump").html(manifestString);
        var k = Object.keys(manifest); // These are the keys. I named them keys
                                       // but that blew up because of conflicts

        for (var i = 0; i < k.length; i++) {
            if(k[i]==="buffer") continue;
            for (var j = 0; j < 6; j++) {
                if(manifest[k[i]][j] !== unoccupied) {
                    $("#teus-inner #row" + (j+1) +" ." + k[i]+" a").html( 
                    manifest[k[i]][j].substr(0, 5) + "..")
                    .removeClass("disabled");
                }
                else {
                    $("#teus-inner #row" + (j+1) +" ." + k[i]+" a")
                    .html("(empty)").addClass("disabled");
                }
            }
        }
    }

    //Upload manifest
    $("#uploadManifestSubmit").click(function () {
        var textManifest = $("#manifestBody").val();
        if (textManifest === "") return;
        steps = [];

        currentManifest = format_manifest(textManifest);
        applyManifest(currentManifest);
        $("#manifestBody").val("");
    });
    
    // Display log history
    $('#viewLogbtn').click(function() {
        try {
          var logs = Ti.Filesystem.getFileStream(Ti.Filesystem.getApplicationDataDirectory(), 'logs.txt');
          logs.open(Ti.Filesystem.MODE_READ);
          var line = logs.readLine();
          var logStr = "";
          do {
              logStr += "<p>" + line + "</a>";
              line = logs.readLine();
          }
          while (line !== null);
          logs.close();
          $("#logSpace").html(logStr);
        }
        catch (e) {
           // statements to handle any exceptions
           console.log("error: "+e); // pass exception object to error handler
        }
    });

    // Populate the list of users
    $("#ch-user-btn").click(function () {
        try {
          var userf = Ti.Filesystem.getFile(Ti.Filesystem.getApplicationDataDirectory(), 'users.txt');
          var users = Ti.Filesystem.getFileStream(Ti.Filesystem.getApplicationDataDirectory(), 'users.txt');
          if (!userf.exists()) {
              users.open(Ti.Filesystem.MODE_WRITE);
              tests = ["1,John,pass",
                      "2,Keogh,password123",
                      "3,Steve,pens"
              ];
              for (var i = 0; i < tests.length; i++) {
                 users.write(tests[i] + '\n');
              }
              users.close();
          }
          //line;
          users.open(Ti.Filesystem.MODE_READ);
          var line = users.readLine();
          var names =[]
          do {
              names.push(line.split(','));
              line = users.readLine();
          }
          while (line !== null);
          users.close();

          var userDisplay = "";
          for (var i = 0; i < names.length; i++) {
              if( names[i][0]==="" ) break;
              var id = names[i][0]
              var name = names[i][1];
              
              userDisplay += '<label class="radio"><input type="radio" ' +
                  ' name="userName" id="userID-' +
                  id + '" value="' +
                  name + '">' + name + '</label>';
         }
         $("#userForm").html(userDisplay + '<input type="password" placeholder="Password" required="required"><br/><button type="submit" class="btn btn-primary">Submit</button>');
      }
      catch (e) {
        // statements to handle any exceptions
        console.log("error: "+e); // pass exception object to error handler
      }
    });
});
