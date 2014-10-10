%define real_name WWW-Search-Lycos
%define upstream_version 2.224

Summary:	WWW::Search::Lycos - class for searching www.lycos.com
Name:		perl-%{real_name}
Version:	%perl_convert_version 2.224
Release: 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/WWW/WWW-Search-Lycos-2.224.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This class is a Lycos specialization of WWW::Search.  It handles
making and interpreting Lycos-site searches http://www.lycos.com.

This class exports no public interface; all interaction should
be done through WWW::Search objects.

%prep
%setup -q -n %{real_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

# make test don't work...
#make test

%install
%makeinstall_std

%files
%doc ChangeLog README
%{perl_vendorlib}/WWW/Search/Lycos.pm
%{_mandir}/*/*



%changelog
* Mon Sep 14 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.223-2mdv2010.0
+ Revision: 440761
- rebuild

* Tue Dec 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.223-1mdv2009.1
+ Revision: 314760
- update to new version 2.223

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.221-6mdv2009.0
+ Revision: 242161
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 2.221-4mdv2008.0
+ Revision: 25466
- rebuild

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 2.221-3mdv2008.0
+ Revision: 23566
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.221-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 2.221-1mdk
- initial Mandriva package


