# https://www.tidytextmining.com/nasa.html#word-co-ocurrences-and-correlations

library(dplyr)
library(tidytext)
library(widyr)
library(jsonlite)

# Load data ---------------------------------------------------------------

metadata <- jsonlite::fromJSON("https://data.nasa.gov/data.json")
names(metadata$dataset)

nasa_title <- data_frame(id = metadata$dataset$`_id`$`$oid`, 
                         title = metadata$dataset$title)

nasa_desc <- data_frame(id = metadata$dataset$`_id`$`$oid`, 
                        desc = metadata$dataset$description)

nasa_keyword <- data_frame(id = metadata$dataset$`_id`$`$oid`, 
                           keyword = metadata$dataset$keyword) %>% 
  unnest(keyword)



# Networks of Description and Title Words ---------------------------------

title_word_pairs <- nasa_title %>% 
  pairwise_count(word, id, sort = TRUE, upper = FALSE)

## # A tibble: 156,689 x 3
##    item1  item2       n
##    <chr>  <chr>   <dbl>
##  1 system project  796.
##  2 lba    eco      683.
##  3 airs   aqua     641.
##  4 level  aqua     623.
##  5 global     resolution 8139.



