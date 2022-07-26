# https://cran.r-project.org/web/packages/subprocess/vignettes/intro.html
# install.packages("subprocess")
library(subprocess)
library(stringr)
library(magrittr)

is_windows <- function () (tolower(.Platform$OS.type) == "windows")

R_binary <- function () {
  R_exe <- ifelse (is_windows(), "R.exe", "R")
  return(file.path(R.home("bin"), R_exe))
}

is_windows <- function () (tolower(.Platform$OS.type) == "windows")

# New a process and terminate

handle <- spawn_process(R_binary(), c('--no-save'))
Sys.sleep(1)
print(handle)
process_terminate(handle)
process_state(handle)  # "terminated"

# Read stdout and stderr

handle <- spawn_process(R_binary(), c('--no-save'))
stdout = process_read(handle, PIPE_STDOUT, timeout = 1000)
stderr = process_read(handle, PIPE_STDERR)
str_c(stdout, collapse = "\n") %>% cat

# Non-interactive command
handle_ls <- spawn_process('/bin/ls')
print(handle_ls)
# Process Handle
# command   : /bin/ls 
# system id : 6203
# state     : exited
process_state(handle_ls)  # state: exited




