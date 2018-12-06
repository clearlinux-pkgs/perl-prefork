#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-prefork
Version  : 1.05
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/prefork-1.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/prefork-1.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libprefork-perl/libprefork-perl_1.04-2.debian.tar.xz
Summary  : 'Optimized module loading for forking or non-forking processes'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-prefork-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution prefork,
version 1.05:
Optimized module loading for forking or non-forking processes

%package dev
Summary: dev components for the perl-prefork package.
Group: Development
Provides: perl-prefork-devel = %{version}-%{release}

%description dev
dev components for the perl-prefork package.


%package license
Summary: license components for the perl-prefork package.
Group: Default

%description license
license components for the perl-prefork package.


%prep
%setup -q -n prefork-1.05
cd ..
%setup -q -T -D -n prefork-1.05 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/prefork-1.05/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-prefork
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-prefork/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1/prefork.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/prefork.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-prefork/LICENSE
