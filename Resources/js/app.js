$(document).ready( function() {
    var window = Ti.UI.currentWindow;
    window.maximize();
    var userName = "";
    // Here we should force a log on
});

// Populate the list of users
$("#ch-user-btn").click( function() {
    /*
    //Open the database first
    var db = Ti.Database.openFile(Ti.Filesystem.getFile(
        Ti.Filesystem.getApplicationDataDirectory(), 'craynedatabase.db'));   
    //Create a table and insert values into it
    db.execute("CREATE TABLE IF NOT EXISTS Users(id INTEGER, userName TEXT)");
    db.execute("INSERT INTO Users VALUES(1,'JoeBloggs')");      

    //Select from Table
    var rows = db.execute("SELECT * FROM Users");
    while (rows.isValidRow()) {
      //Alert the value of fields id and firstName from the Users database
      alert('The user id is '+ 
        rows.fieldByName('id')+
        ', and user name is '+
        rows.fieldByName('userName'));
	    rows.next();
	    var id = rows.fieldByName('id');
	    var name =rows.fieldByName('userName');
	    $("#userForm").prepend('<input type="radio" name="userName" id="userID-'+
                         	    id+'" value="'+
        	                    name+'" checked>'+name+'</label>');
      rows.close();
      Db.close();
    }*/  	                    
    //Check for existance of a file
    var users = Ti.Filesystem.getFile(Ti.Filesystem.getApplicationDataDirectory(),'users.txt');
    var names = [];
    if(!document.exists()) {
      users.open(Ti.Filesystem.MODE_WRITE);
      tests = [ "1,John",
                "2,Keogh",
                "3,Steve"];
      for( var i = 0; i < tests.length; i++ ) {
        users.write(tests[i]+'\n');
      }
      users.close();
    }
    var line;
    do {
      line = users.readLine();
      names.push(line.split(','));
    }
    while(line!==null);  

    for( var i=0; i<names.length; i++) {
      var id = names[i][0]
	    var name = names[i][1];
	    $("#userForm").prepend('<input type="radio" name="userName" id="userID-'+
                         	    id+'" value="'+
        	                    name+'" checked>'+name+'</label>');
    }
});
