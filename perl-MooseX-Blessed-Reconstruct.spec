%define upstream_name    MooseX-Blessed-Reconstruct
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A L<Data::Visitor> for creating Moose objects
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::MOP)
BuildRequires:	perl(Data::Visitor)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
The purpose of this module is to "fix up" blessed data into a real Moose
object.

This is used internally by the MooseX::YAML manpage but has no
implementation details having to do with the YAML manpage itself.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 653601
- rebuild for updated spec-helper

* Wed Jul 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 562775
- import perl-MooseX-Blessed-Reconstruct


* Wed Jul 14 2010 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
