Rem Programul imi face un backUp unde am nevoie
Rem 7z a TheWord_ModuleByZah.zip D:\TW5\Module_by_Zah
Rem echo "Am terminat The Word_ModuleByZah"
7z a TheWord_backUp.zip D:\TW5\Zah  
echo "Am terminat The Word_ScrisByZah"
7z a KeyNoteNF_backUp.zip D:\KEYNOTE\DATABASE
echo "Am terminat KeyWordNF"
pause

Rem 7z <command> [<switches>...] <archive_name> [<file_names>...] [@listfile]

Rem     set the path to computer
Rem     Right click on MyComputer > Properties >
Rem     > Advanced system setting > Advanced > Enviromet variable > 
Rem     > System variable > Path > Edit > ;C:\Program Files\7-Zip

Rem         sau in CMD
Rem     set PATH=%PATH%;C:\Program Files\7-Zip\
Rem     echo %PATH%

Rem Examples:
Rem         7z a archive1.zip subdir\
Rem adds all files and subfolders from folder subdir to archive archive1.zip. 
Rem The filenames in archive will contain subdir\ prefix.

Rem         7z a archive2.zip .\subdir\*
Rem adds all files and subfolders from folder subdir to archive archive2.zip. 
Rem The filenames in archive will not contain subdir\ prefix.

Rem         cd /D c:\dir1\
Rem         7z a c:\archive3.zip dir2\dir3\ 
Rem The filenames in archive c:\archive3.zip will contain dir2\dir3\ prefix, 
Rem but they will not contain c:\dir1\ prefix.

Rem         7z a Files.7z *.txt -r
Rem adds all *.txt files from current folder and its subfolders to archive Files.7z.

Rem Notes:
Rem 7-Zip doesn't use the system wildcard parser. 7-Zip doesn't follow the 
Rem archaic rule by which *.* means any file. 7-Zip treats *.* as matching the 
Rem name of any file that has an extension. To process all files, you must use a * wildcard.

Rem    <Commands>
Rem      a : Add files to archive
Rem      b : Benchmark
Rem      d : Delete files from archive
Rem      e : Extract files from archive (without using directory names)
Rem      h : Calculate hash values for files
Rem      i : Show information about supported formats
Rem      l : List contents of archive
Rem      rn : Rename files in archive
Rem      t : Test integrity of archive
Rem      u : Update files to archive
Rem      x : eXtract files with full paths
Rem    
Rem    <Switches>
Rem      -- : Stop switches and @listfile parsing
Rem      -ai[r[-|0]]{@listfile|!wildcard} : Include archives
Rem      -ax[r[-|0]]{@listfile|!wildcard} : eXclude archives
Rem      -ao{a|s|t|u} : set Overwrite mode
Rem      -an : disable archive_name field
Rem      -bb[0-3] : set output log level
Rem      -bd : disable progress indicator
Rem      -bs{o|e|p}{0|1|2} : set output stream for output/error/progress line
Rem      -bt : show execution time statistics
Rem      -i[r[-|0]]{@listfile|!wildcard} : Include filenames
Rem      -m{Parameters} : set compression Method
Rem        -mmt[N] : set number of CPU threads
Rem        -mx[N] : set compression level: -mx1 (fastest) ... -mx9 (ultra)
Rem      -o{Directory} : set Output directory
Rem      -p{Password} : set Password
Rem      -r[-|0] : Recurse subdirectories
Rem      -sa{a|e|s} : set Archive name mode
Rem      -scc{UTF-8|WIN|DOS} : set charset for for console input/output
Rem      -scs{UTF-8|UTF-16LE|UTF-16BE|WIN|DOS|{id}} : set charset for list files
Rem      -scrc[CRC32|CRC64|SHA1|SHA256|*] : set hash function for x, e, h commands
Rem      -sdel : delete files after compression
Rem      -seml[.] : send archive by email
Rem      -sfx[{name}] : Create SFX archive
Rem      -si[{name}] : read data from stdin
Rem      -slp : set Large Pages mode
Rem      -slt : show technical information for l (List) command
Rem      -snh : store hard links as links
Rem      -snl : store symbolic links as links
Rem      -sni : store NT security information
Rem      -sns[-] : store NTFS alternate streams
Rem      -so : write data to stdout
Rem      -spd : disable wildcard matching for file names
Rem      -spe : eliminate duplication of root folder for extract command
Rem      -spf : use fully qualified file paths
Rem      -ssc[-] : set sensitive case mode
Rem      -sse : stop archive creating, if it can't open some input file
Rem      -ssw : compress shared files
Rem      -stl : set archive timestamp from the most recently modified file
Rem      -stm{HexMask} : set CPU thread affinity mask (hexadecimal number)
Rem      -stx{Type} : exclude archive type
Rem      -t{Type} : Set type of archive
Rem      -u[-][p#][q#][r#][x#][y#][z#][!newArchiveName] : Update options
Rem      -v{Size}[b|k|m|g] : Create volumes
Rem      -w[{path}] : assign Work directory. Empty path means a temporary directory
Rem      -x[r[-|0]]{@listfile|!wildcard} : eXclude filenames
Rem      -y : assume Yes on all queries