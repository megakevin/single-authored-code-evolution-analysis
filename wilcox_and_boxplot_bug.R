project = "wordpress-android"

data <- read.csv(paste("/home/kevin/Desktop/evolution-project/data/stats/overall/stats-", 
                       project ,
                       ".csv", 
                       sep=""), 
                 header = TRUE);

sac <- subset(data, is_sac == 'True' & bug_commit_num > 0);
non_sac <- subset(data, is_sac == 'False' & bug_commit_num > 0);

summary(sac$bug_commit_num);
summary(non_sac$bug_commit_num);

test_result = wilcox.test(sac$bug_commit_num, non_sac$bug_commit_num, paired=FALSE, alternative="greater", conf.int=TRUE);
test_result;

png(paste("/home/kevin/Desktop/evolution-project/data/stats/overall/stats-", 
          project, 
          ".png", 
          sep=""))
boxplot(sac$bug_commit_num, non_sac$bug_commit_num);
dev.off()

paste(project, 
      median(sac$bug_commit_num), 
      median(non_sac$bug_commit_num), 
      test_result$estimate,
      test_result$p.value,
      sep = ",");