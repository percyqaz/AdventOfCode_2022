data Line = Up
          | Down String
          | Root
          | List
          | NewFile String Int
          | NewDir String
            deriving Show

data FileSystem = FsDir String [FileSystem]
                | FsFile String Int
                  deriving Show
                
type DirectoryPointer = [String]
type State = (FileSystem, DirectoryPointer)
                
add_to_fs :: DirectoryPointer -> FileSystem -> FileSystem -> FileSystem

add_to_fs [] item (FsDir name entries) =
    FsDir name (item : entries)
    
add_to_fs (p : ps) item (FsDir name entries) =
    FsDir name (map (add_to_fs' (p : ps) item) entries)
    
-- This one conditionally applies changes to subdirectories
add_to_fs' :: DirectoryPointer -> FileSystem -> FileSystem -> FileSystem
    
add_to_fs' (directory_name : ptr) item target =
    case target of
        FsDir name entries -> 
            if name == directory_name then add_to_fs ptr item target
            else target
        _ -> target

parse_line :: String -> Line

parse_line ln =
    case words ln of
        ["$", "cd", "/"] -> Root
        ["$", "cd", ".."] -> Up
        ["$", "cd", s] -> Down s
        ["$", "ls"] -> List
        ["dir", s] -> NewDir s
        [size, file] -> NewFile file (read size :: Int)

line :: State -> String -> State

line (fs, ptr) ln =
    case parse_line ln of
        Root -> (fs, [])
        Down s -> (fs, (s : ptr))
        Up -> (fs, tail ptr)
        List -> (fs, ptr)
        NewFile name size -> (add_to_fs (reverse ptr) (FsFile name size) fs, ptr)
        NewDir name -> (add_to_fs (reverse ptr) (FsDir name []) fs, ptr)
        
format' :: Int -> FileSystem -> [String]
        
format' indent (FsDir name entries) =
    (replicate indent ' ' ++ "- " ++ name ++ " (dir)") : concat (map (format' (indent + 2)) entries)
    
format' indent (FsFile name size) =
    (replicate indent ' ' ++ "- " ++ name ++ " (file, size=" ++ show size ++ ")") : []

format fs = format' 0 fs

---

size_of (FsFile name size) = size
size_of (FsDir name entries) = sum . (map size_of) $ entries

count_sizes (FsDir name entries) =
    let this_directory_size = size_of (FsDir name entries) in
    let totals = sum . (map count_sizes) $ entries in
    
    if this_directory_size <= 100000 then this_directory_size + totals
    else totals
    
count_sizes (FsFile name size) = 0

main :: IO ()
main = do 
    txt <- readFile $ "test_data.txt"
    let the_files = fst $ foldl line (FsDir "/" [], []) (lines $ txt)
    haskell_truly_is_something <- sequence . (map print) . format $ the_files
    print . show . count_sizes $ the_files
    print $ "Done"