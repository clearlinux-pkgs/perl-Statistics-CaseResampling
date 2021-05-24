#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Statistics-CaseResampling
Version  : 0.15
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Statistics-CaseResampling-0.15.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Statistics-CaseResampling-0.15.tar.gz
Summary  : 'Efficient resampling and calculation of medians with confidence intervals'
Group    : Development/Tools
License  : GPL-1.0
Requires: perl-Statistics-CaseResampling-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Statistics::CaseResampling - Efficient resampling and calculation of
medians with confidence intervals

%package dev
Summary: dev components for the perl-Statistics-CaseResampling package.
Group: Development
Provides: perl-Statistics-CaseResampling-devel = %{version}-%{release}
Requires: perl-Statistics-CaseResampling = %{version}-%{release}

%description dev
dev components for the perl-Statistics-CaseResampling package.


%package perl
Summary: perl components for the perl-Statistics-CaseResampling package.
Group: Default
Requires: perl-Statistics-CaseResampling = %{version}-%{release}

%description perl
perl components for the perl-Statistics-CaseResampling package.


%prep
%setup -q -n Statistics-CaseResampling-0.15
cd %{_builddir}/Statistics-CaseResampling-0.15

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Statistics::CaseResampling.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Statistics/CaseResampling.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Statistics/CaseResampling/CaseResampling.so
