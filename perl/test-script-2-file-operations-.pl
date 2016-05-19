#!/usr/bin/perl
#open,read ,write,append,copy,rename,filesize
open (FILE,"C:/file5.txt") or die("ERROR");
@array = <FILE>;
print @array;
close(FILE);
foreach $line (@array)
{
chomp($line);
$line = uc($line);
print "$line\n";
if($line =~/Tes/i){print "yes\n";}
else{print "no \n";}
}
open (FILE,">>C:/file.txt");
flock(FILE,2); #lock file writing to user
print FILE "hekko\n";
close(FILE);

rename "C:/file.txt","C:/file2.txt";
use File::Copy;
copy("C:/file2.txt","C:/file.txt");
unlink "C:/file2.txt"; #delete file2
$file = "C:/file.txt";
$size = (stat $file)[7];
print "File is $size bytes\n";

#hash
@arrat = (1..10);
@aray2=((1..5),(5,4,3));
%hash2 = map{$_=>1}@aray2;
print "@{[%hash2]}\n". "\n@aray2\n";
 while ( my ($key, $value) = each(%hash2) ) {
        print "$key => $value\n";
    }
