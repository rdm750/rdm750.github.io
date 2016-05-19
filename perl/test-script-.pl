#!/usr/bin/perl
print "Content-type: text/html\n\n";
print "<html><h1>Hello!</h1></html>\n";
print "Hello World \n";
($word1,$word2) = ("Perl","Tutorial");
 $word3 = "$word1 $word2 \n";
 print $word3;
 @testnumbers = (1...10);
 print "\n@testnumbers\n";
 @numbers = (1,2,3,"test",5);
 $numbers[6] = 3;
 $test = $numbers[0] + $numbers[2];
 print "\n $numbers[0] $test $#numbers \n @numbers \n"; #length of array - 1  #merge,reverse,sort,push,pop,shift,unshift arrays
 $#numbers = 2;
 print "@numbers \n"; #length of array
 #@numbers = ();
 #print "\n $#numbers \n @numbers \n"; #length of array+ array print
 push (@numbers,"hello");
 print "\n $#numbers \n @numbers \n"; #length of array     + array print
 pop (@numbers);
 print "\n $#numbers \n @numbers \n"; #length of array+ array print
 unshift (@numbers,"hello");
 print "\n $#numbers \n @numbers \n"; #length of array + array print
 shift (@numbers);
 print "\n $#numbers \n @numbers \n"; #length of array  + array print
 @numbers1 = (4,2,7,"test",5,6,"world");
 @numbers3 = (@numbers,@numbers1);
 @reversed = reverse(@numbers3);
 print "\n $#numbers3 \n @reversed \n"; #length of array  + array print #merge,reverse,sort,push,pop,shift,unshift arrays
 $#numbers1 = 2;
 @sorted = sort{$a <=> $b}(@numbers1);
 print "\n $#numbers1 \n @sorted \n"; #length of array  + array print
 @words1 = qw(green test world);
 @sorted1 = sort{$a cmp $b}(@words1);
 print "\n $#words1 \n @sorted1 \n"; #length of array  + array print
 @array = (Hello) x 100;
 print "@array \n";
 $count1 =1;                #Loops foreach elsif if unless while
 foreach $word (@words1)
 {
 print "$count1 $word\n";
 $count1++;
 }
 $tnumber =10;
 $tnumber1 =10;
 if ($tnumber > 10){print "greater";}
 elsif ($tnumber < 10) {print "less";}
 else {print "number is 10 \n";}
 unless ($tnumber == 10) { print "number is not 10";}
 else {print "number is 10 \n";}
 use integer;
 print ((2+4/2+(1-2)*4+7)%4)*1.333 . "\n";        #operators math exponent increment decrement
 print "\n" . $tnumber-- . "\n" . $tnumber . "\n";
 $letter = "A";
 print $letter++ . "\n" . $letter . "\n";
 while ($tnumber > 3){ print "\n" . $tnumber-- . "hello \n";}
 until ($tnumber1 == 5){ print "\n" . $tnumber1-- . "hello \n";}
 # map act on all items in array, grep hash (keys,values)
 @array = qw(apple orange banana plum);
 map {$_ = uc($_)} (@array);
 @array2 = grep {$_ =~ "N"} @array;
 print "@array2\n";
 if (101 .. 200) { print; }        # print 2nd hundred lines
 %hash = ();
 $hash{name} = john;
 $hash{age} = 25;
 $hash{city}= london;
 print "@{[%hash]}\n";
 %hash2 = qw(name john age 26 city);
 print "@{[%hash2]}\n";
 while (($key,$value) = each(%hash2)){print "$key = $ value\n"}
 foreach $key (keys %hash2) {print "$key\n"};
 if (exists ($hash2{city})){print "does exist\n";} #hash exist and defined
 if (defined ($hash2{city})){print "does exist and defined\n";}
 else {print "not defined\n"}
 delete($hash2{city});
 if (exists ($hash2{city})){print "does exist\n";} #hash exist and defined
 else {print "not exist\n"}
 if (defined ($hash2{city})){print "does exist and defined\n";}
 else {print "not defined\n"}
foreach $key (sort keys %hash) {
print "$key\n";}
%reversed = reverse %hash;
foreach $key (keys %reversed) {
print "$key - $reversed{$key}\n";}
%hash3 = (%reversed,%hash);
print "@{[%hash2]}\n";
$words = "the cat is white";
($w1,$w2,$w3,$w4) = split(/ /,$words);
print "$w1\n";
@warray = ($w1,$w2,$w3,$w4);
#$joined = join(" ",("$w1","$w2","$w3","$w4"));
$joined = join(" ",(@warray));
 print "$joined\n". "test\n";
#lc,uc, lowercase uppercase functions uc($words) lcfirst,ucfirst
$words = join (' ',
map {ucfirst lc}split(/ /,$words));
print "$words\n"; #length,substring,index of strings,random, int rand,sprintf rounding,localtime(time)
#regex i= case insensetive m = modify; s = substition modifier;t = translation modifer;
$string = "hEre Is a STrinG";
if ($string =~ m/here is a string/i) {print "match!\n";}
$string =~ s/here/THere/i;   #o+ multiple o replaced with something else g = globally
$string =~ s/H+/t/g;
print "$string\n";
#search for character class and numbers in string
#removing leading and trailing whitespaces, $string=~s/^\s+//,$string=~s/\s+//
$number ="123";
if ($number =~ /^\d+$/){
print "It's a number!\n";
}
$number ="RasdD";
if ($number =~ /^[A-Za-z]+$/){
print "found letters!\n";
}
sub doit { print "test\n";}
doit;
 exit;