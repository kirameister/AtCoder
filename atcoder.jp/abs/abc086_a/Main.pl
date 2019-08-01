use strict;
my $line = <STDIN>;
chomp($line);
my @nums = split(/ /, $line);
if( ($nums[0]*$nums[1]) % 2 == 0){
	print("Even\n");
}else{
	print("Odd\n");
}