#' Install/update necessary packages from CRAN, GitHub
#'
#' @param packages a vector of strings with names of packages from CRAN, Bioconductor, GitHub
#' @param file a file with packages; overrides packages parameter
#' @param update_packages whether to update existing packages (Default: FALSE)
#' @param repos the CRAN repository to use
#' @param dry_run whether to test for missing packages (Default: FALSE)
#'
#' @example
#' \dontrun {
#' source("https://gist.githubusercontent.com/cannin/6b8c68e7db19c4902459/raw/installPackages.R")
#' install_requirements("r-requirements.txt")
#' }
install_requirements <- function(
  file=NULL, packages=NULL, update_packages=FALSE, type=getOption("pkgType"),
  repos=NULL, dry_run=FALSE) {
  # file = "R-requirements.txt"

  # setRepositories(ind=1:6)
  available_packages <- rownames(available.packages())
  installed_packages <- rownames(installed.packages())

  if (!is.null(repos)) {
    options(repos=repos, unzip="internal") # unzip needed for Ubuntu
  }

  # Install packages
  if(!is.null(file)) {
    packages <- read.table(file, stringsAsFactors = FALSE, encoding = "UTF-8")
    packages <- packages$V1
    cat("Packages:", fill = TRUE)
    cat(packages, sep=", ", fill = TRUE)
  }

  if("devtools" %in% rownames(installed.packages())) {
    require(devtools)
  } else {
    install.packages("devtools")
    require(devtools)
  }

  if("stringr" %in% rownames(installed.packages())) {
    require(stringr)
  } else {
    install_cran("stringr")
    require(devtools)
  }

  if(!dryRun) {
    for(package in packages) {
      tmp <- strsplit(package, .Platform$file.sep)[[1]]
      package_name <- tmp[length(tmp)]

      if(!(package_name %in% installed_packages)) {
        tryCatch({
          if(package %in% available_packages) {
            if(update_packages) {
              cat("Update packages ...", fill = TRUE)
              update.packages(ask = FALSE)
            }
            install_cran(package, type=type)
          } else if(str_count(package, '/') == 1) {
            if(str_count(package, 'github') == 1) {
              tmpPkg <- strsplit(package, ":")[[1]][2]
              cat("install_github:", tmpPkg, fill = TRUE)
              install_github(tmpPkg, upgrade=update_packages)
            } else if(str_count(package, 'bitbucket') == 1) {
              tmpPkg <- strsplit(package, ":")[[1]][2]
              cat("install_bitbucket", tmpPkg, fill = TRUE)
              install_bitbucket(tmpPkg, upgrade=update_packages)
            } else {
              cat("install_github:", package, fill = TRUE)
              install_github(package, upgrade=update_packages)
            }
          } else if(str_count(package, .Platform$file.sep) > 1) {
            install(package, type="source")
          } else {
            cat("ERROR: Package: ", package, "\n")
          }

          # Try to test if rJava worked
          # NOTE: Requires additional steps: https://stackoverflow.com/questions/30738974/rjava-load-error-in-rstudio-r-after-upgrading-to-osx-yosemite
          if(packageName == "rJava") {
            library(rJava)
            .jinit()
          }
        }, error = function(e) {
          cat("ERROR: Package: ", package, ". Message: ", message(e), "\n")
        })
      } else {
        cat("Already installed: ", package, "\n")
      }
    }
  }
}
