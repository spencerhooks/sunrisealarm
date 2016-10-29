# sunrisealarm
Small project to create a lamp that simulates the sunrise to help wake me up in the winter. Using a MiPow PlayBulb Rainbow and running on a Raspberry Pi 2 with USB bluetooth adaptor.

This branch uses Cron to schedule the sunrise and uses pygatt rather than the bash command gatttool to send bluetooth commands.