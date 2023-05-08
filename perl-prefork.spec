#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-prefork
Version  : 1.05
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/prefork-1.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/prefork-1.05.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libprefork-perl/libprefork-perl_1.04-2.debian.tar.xz
Summary  : 'Optimized module loading for forking or non-forking processes'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-prefork-license = %{version}-%{release}
Requires: perl-prefork-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution prefork,
version 1.05:
Optimized module loading for forking or non-forking processes

%package dev
Summary: dev components for the perl-prefork package.
Group: Development
Provides: perl-prefork-devel = %{version}-%{release}
Requires: perl-prefork = %{version}-%{release}

%description dev
dev components for the perl-prefork package.


%package license
Summary: license components for the perl-prefork package.
Group: Default

%description license
license components for the perl-prefork package.


%package perl
Summary: perl components for the perl-prefork package.
Group: Default
Requires: perl-prefork = %{version}-%{release}

%description perl
perl components for the perl-prefork package.


%prep
%setup -q -n prefork-1.05
cd %{_builddir}
tar xf %{_sourcedir}/libprefork-perl_1.04-2.debian.tar.xz
cd %{_builddir}/prefork-1.05
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/prefork-1.05/deblicense/

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-prefork
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-prefork/82c7a4a874eacce070f1fd5fefae53f8ce04b459
cp %{_builddir}/prefork-1.05/LICENSE %{buildroot}/usr/share/package-licenses/perl-prefork/b49005c259b7d098d7002eb25909e01a2f94426f
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
/usr/share/man/man3/prefork.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-prefork/82c7a4a874eacce070f1fd5fefae53f8ce04b459
/usr/share/package-licenses/perl-prefork/b49005c259b7d098d7002eb25909e01a2f94426f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
