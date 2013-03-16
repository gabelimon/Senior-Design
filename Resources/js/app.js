$(document).ready( function() {
    var window = Ti.UI.currentWindow;
    window.maximize();
    userName = "";
    // Here we should force a log on
});

// Populate the list of users
$("#ch-user-btn").click( function() {
    //Open the database first
    var db = Ti.Database.openFile(Ti.Filesystem.getFile(
        Ti.Filesystem.getApplicationDataDirectory(), 'customdatabase.db'));   

    //Create a table and insert values into it
    db.execute("CREATE TABLE IF NOT EXISTS Users(id INTEGER, firstName TEXT)");
    db.execute("INSERT INTO Users VALUES(1,'Joe Bloggs')");      

    //Select from Table
    var rows = db.execute("SELECT * FROM Users");
    while (rows.isValidRow()) {
	//Alert the value of fields id and firstName from the Users database
	alert('The user id is '+
	      rows.fieldByName('id')+
	      ', and user name is '
	      +rows.fieldByName('firstName'));
	rows.next();    
    }

    //Release memory once you are done with the resultset and the database
    rows.close();
    db.close();
});