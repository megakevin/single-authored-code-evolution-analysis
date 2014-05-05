project = "wordpress-android"

data <- read.csv(paste("/home/kevin/Desktop/evolution-project/data/stats/overall/stats-", 
                       project ,
                       ".csv", 
                       sep=""), 
                 header = TRUE);

sac <- subset(data, is_sac == 'True' & commit_num >= 0);
non_sac <- subset(data, is_sac == 'False' & commit_num >= 0);

summary(sac$commit_num);
summary(non_sac$commit_num);

test_result = wilcox.test(sac$commit_num, non_sac$commit_num, paired=FALSE, alternative="greater", conf.int=TRUE);
test_result;

png(paste("/home/kevin/Desktop/evolution-project/data/stats/overall/stats-", 
          project, 
          ".png", 
          sep=""))
boxplot(sac$commit_num, non_sac$commit_num, log="y");
dev.off()

paste(project, 
      median(sac$commit_num), 
      median(non_sac$commit_num), 
      test_result$estimate,
      test_result$p.value,
      sep = ",");