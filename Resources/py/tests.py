from functions import *

test_file = open("test/Manifest_Wicklow_Way.txt")
test_manifest_string = test_file.read()
test_file.close()

test_manifest = format_manifest( test_manifest_string )
test_box_pos = ['A', 5]

removed_TEU_file = open("test/Manifest_Wicklow_Way_removed.txt")
removed_TEU_string = removed_TEU_file.read()
removed_TEU_file.close()
removed_manifest = format_manifest( removed_TEU_string )

    #TESTING REMOVE
if( remove_box(test_manifest, test_box_pos) != removed_manifest ):
    raise Exception("Removal failed")

    #TESTING INSERT
if( insert_box(removed_manifest, 'Jones, chrome') != test_manifest):
    raise Exception("Insertion failed")


    #Repeating the tests
test_file = open("test/Manifest_Savannah_Express.txt")
test_manifest_string = test_file.read()
test_file.close()

test_manifest = format_manifest( test_manifest_string )

removed_TEU_file = open("test/Manifest_Savannah_Express_removed.txt")
removed_TEU_string = removed_TEU_file.read()
removed_TEU_file.close()
removed_manifest = format_manifest( removed_TEU_string )

test_box_pos = ["A", 1]
    #TESTING REMOVE
if( remove_box(test_manifest, test_box_pos) != removed_manifest ):
    raise Exception("Removal failed")

    #TESTING INSERT
if( insert_box(removed_manifest, 'Walmart, tires and carpets') != test_manifest):
    raise Exception("Insertion failed")


print "Tests passed"
