install.packages(c('curl', 'repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest','RStoolbox'))
devtools::install_github('IRkernel/IRkernel')
IRkernel::installspec(user = FALSE)
