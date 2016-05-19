#!/usr/bin/perl

#test script to extract data

opendir(DIR, "C:/test");
@files = readdir(DIR);
closedir(DIR);

while( ($filename = readdir(DIR))){
     print("$filename\n");
}

foreach $fil (@files) {
  # put your perl code here
  #a? means: match 'a' 1 or 0 times a* means: match 'a' 0 or more times, i.e., any number of times
#a+ means: match 'a' 1 or more times, i.e., at least onc
  if($fil !~ m/^\.+/i)
         {
 print file2 "-------------**************-------------\n";

#open (FILE,"C:/test_element1.txt") or die("ERROR");
$stringt = "C:\\test\\$fil";
#open (FILE,"C:\\test\\test_element_1_1082012_Time.txt") or die("ERROR");
open (FILE,$stringt) or die("ERROR");
@array = <FILE>;
close(FILE);

open (file2,">>C:/file-test_element-output-2.txt");

print file2 "$fil\n";
%hash = ();
foreach $line (@array)
{
      $flag = 0;
     chomp($line);
     if($line =~m/VPPA/i && $line !~ m/UNLOCK/i)
         {
              @test1 = split(/ /,$line);
              print file2 "$line\n";
              foreach $item (@test1)
               {
                 if($item =~m/VPPA/i) #$item =~ /^\d+$/
                 {
                   $flag++;
                   $item2=$item;
                 }
                 else
                 {}
               }


               $hash{$item2} = $test1[-3];
               print file2 "\n".$item2.",".$test1[-3]."\n";

         }
     else{}
}
print file2 "-------------\n".$flag."-------------\n";
print file2 "-------------**************-------------\n";
print file2 "@{[%hash]}\n";
close(file2);
}

}